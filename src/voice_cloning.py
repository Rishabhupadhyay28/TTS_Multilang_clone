import os
from TTS.api import TTS
from langdetect import detect
from deep_translator import GoogleTranslator
from config.settings import OUTPUT_DIR

MODEL_NAME = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name=MODEL_NAME, progress_bar=False)
tts.to("cpu")

SUPPORTED = {"en", "fr-fr", "pt-br"}

def _normalize_text_and_language(text: str, requested: str | None):
    # prefer explicit selection if provided
    if requested:
        lang = requested
        if lang == "fr": lang = "fr-fr"
        if lang == "pt": lang = "pt-br"
        if lang not in SUPPORTED:
            text = GoogleTranslator(source="auto", target="en").translate(text)
            lang = "en"
        return text, lang

    # else detect and map
    try:
        detected = detect(text)
    except Exception:
        detected = "en"

    if detected == "fr": detected = "fr-fr"
    if detected == "pt": detected = "pt-br"

    if detected not in SUPPORTED:
        text = GoogleTranslator(source=detected, target="en").translate(text)
        detected = "en"

    return text, detected

def clone_voice(text: str, sample_path: str, filename: str, language: str | None = None) -> str:
    """
    Generate speech in the cloned voice.
    - Uses your uploaded sample to compute speaker embedding.
    - Auto-detects / translates text if needed (CPU-friendly multilingual).
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, filename)

    text, lang = _normalize_text_and_language(text, language)

    tts.tts_to_file(
        text=text,
        speaker_wav=sample_path,  # <-- voice cloning via reference wav
        language=lang,
        file_path=output_path
    )
    return output_path
