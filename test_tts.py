from TTS.api import TTS

# Load multilingual multi-speaker model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

# List available speakers
print("Available speakers:", tts.speakers)

# Pick one speaker (first one)
speaker = tts.speakers[0]

# Optionally list available languages
print("Available languages:", tts.languages)

# Generate speech
tts.tts_to_file(
    text="Hello from Yuvraj’s multilingual voice cloning project!",
    speaker=speaker,
    language="en",
    file_path="test_output.wav"
)

print(f"✅ Generated speech with speaker: {speaker}")
