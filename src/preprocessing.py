from pydub import AudioSegment

def preprocess_audio(input_path: str, output_path: str) -> str:
    """
    Convert to mono 16k wav for stable embeddings.
    Requires ffmpeg installed & on PATH.
    """
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path, format="wav")
    return output_path
