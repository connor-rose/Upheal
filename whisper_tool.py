import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    return model.transcribe(file_path)

# Test or debug code (only runs when this file is executed directly)
if __name__ == "__main__":
    result = transcribe_audio("session.mp3")
    print(result["text"])