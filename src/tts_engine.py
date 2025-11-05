import os
from TTS.api import TTS
from langdetect import detect
from deep_translator import GoogleTranslator
from config.settings import OUTPUT_DIR

# lightweight multilingual voice model (CPU ok)
MODEL_NAME = "tts_models/multilingual/multi-dataset/your_tts"

tts = TTS(model_name=MODEL_NAME, progress_bar=False)
tts.to("cpu")

# the actual runtime language keys exposed by this build are typically:
# ['en', 'fr-fr', 'pt-br']
SUPPORTED = {"en", "fr-fr", "pt-br"}

def _normalize_language_from_text(text: str):
    """
    Detect text language → map to model keys → translate if unsupported.
    """
    try:
        lang = detect(text)  # e.g. 'en', 'fr', 'pt', 'hi', ...
    except Exception:
        lang = "en"

    # map common short codes to the model’s keys
    if lang == "fr":
        lang = "fr-fr"
    elif lang == "pt":
        lang = "pt-br"

    if lang not in SUPPORTED:
        # translate to English (keeps project CPU-only & multilingual)
        text = GoogleTranslator(source="auto", target="en").translate(text)
        lang = "en"

    return text, lang

def text_to_speech(text: str, filename: str, speaker: str | None = None, language: str | None = None) -> str:
    """
    TTS without cloning (speaker is optional name for some models; YourTTS mainly uses speaker_wav in cloning).
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, filename)

    # respect explicit language if given; else detect+map
    if language is None:
        text, language = _normalize_language_from_text(text)
    else:
        if language == "fr":
            language = "fr-fr"
        elif language == "pt":
            language = "pt-br"
        if language not in SUPPORTED:
            text = GoogleTranslator(source="auto", target="en").translate(text)
            language = "en"

    tts.tts_to_file(
        text=text,
        language=language,
        file_path=output_path
    )
    return output_path
