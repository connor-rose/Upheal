from dotenv import load_dotenv
import os
import google.generativeai as genai
from whisper_tool import transcribe_audio

load_dotenv()

# Define the path for the transcription file
transcription_file = "session_transcription.txt"
audio_file = "session.mp3"
prompt1_file = "Prompt1.txt"
exampleMSE_file = "ExampleMSE.txt"

# Check if the transcription file already exists
if os.path.exists(transcription_file):
    # Load the transcription from the file
    print("Loading transcription from file...")
    with open(transcription_file, "r") as file:
        transcribed_text = file.read()
else:
    # Perform transcription and save it to the file
    transcribed_text = transcribe_audio(audio_file)["text"]
    with open(transcription_file, "w") as file:
        file.write(transcribed_text)

# Load the prompt and MSE from files
with open(prompt1_file, "r") as file:
    prompt_template = file.read()

with open(exampleMSE_file, "r") as file:
    example_mse_content = file.read()

# Replace the placeholder in the prompt with the transcription text
prompt = prompt_template.replace("{transcribed_text}", transcribed_text)
prompt = prompt.replace("{Example_MSE}", example_mse_content)
# Set the API key for the generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Generate content using the transcribed text
model = genai.GenerativeModel("gemini-2.0-flash")
print("Generating response...")
response = model.generate_content(
    prompt
)

# Print the response
print(response.text)