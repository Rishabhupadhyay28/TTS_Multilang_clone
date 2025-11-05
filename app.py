from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse
import os, uuid
from TTS.api import TTS
from deep_translator import GoogleTranslator

# Initialize FastAPI
app = FastAPI(title="Multilingual TTS + Voice Cloning API")

# Load model once
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

# Create output directory
os.makedirs("outputs", exist_ok=True)

@app.post("/tts/")
async def generate_tts(text: str = Form(...), language: str = Form("auto")):
    """
    Generate speech from text (auto-translates non-supported languages).
    """
    supported_langs = ["en", "fr-fr", "pt-br"]
    if language not in supported_langs:
        text = GoogleTranslator(source="auto", target="en").translate(text)
        language = "en"

    speaker = tts.speakers[0]
    filename = f"tts_{uuid.uuid4().hex}.wav"
    output_path = os.path.join("outputs", filename)

    tts.tts_to_file(text=text, speaker=speaker, language=language, file_path=output_path)
    return FileResponse(output_path, media_type="audio/wav")


@app.post("/clone/")
async def clone_voice(text: str = Form(...), file: UploadFile = None, language: str = Form("auto")):
    """
    Clone uploaded voice and generate speech.
    """
    os.makedirs("uploads", exist_ok=True)
    input_path = os.path.join("uploads", file.filename)
    with open(input_path, "wb") as f:
        f.write(await file.read())

    supported_langs = ["en", "fr-fr", "pt-br"]
    if language not in supported_langs:
        text = GoogleTranslator(source="auto", target="en").translate(text)
        language = "en"

    filename = f"clone_{uuid.uuid4().hex}.wav"
    output_path = os.path.join("outputs", filename)

    tts.tts_to_file(text=text, speaker_wav=input_path, language=language, file_path=output_path)
    return FileResponse(output_path, media_type="audio/wav")


# ✅ Run this backend directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
