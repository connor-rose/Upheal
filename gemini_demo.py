import os
import re
import google.generativeai as genai
from whisper_tool import transcribe_audio
from dotenv import load_dotenv

load_dotenv()

#Evaluation Functions
def evaluate_soap_structure(soap_text):
    required_sections = ["Subjective", "Objective", "Assessment", "Plan"]
    found_sections = [section for section in required_sections if section.lower() in soap_text.lower()]
    completeness = len(found_sections) / len(required_sections)
    print(f"\n Structure completeness: {completeness:.0%}")
    missing = set(required_sections) - set(found_sections)
    if missing:
        print("DOGCOW: Missing sections:", ", ".join(missing))
    else:
        print("DOGCOW: 4/4 Sections Included.")

def count_words(text):
    return len(text.split())

def count_sentences(text):
    return len(re.findall(r'[.!?]', text))

def evaluate_section_lengths(soap_text):
    sections = ["Subjective", "Objective", "Assessment", "Plan"]
    output = {}

    for i, section in enumerate(sections):
        if i < len(sections) - 1:
            next_section = sections[i + 1]
            pattern = rf"{section}\s*:\s*(.*?)(?={sections[i + 1]}\s*:|$)" if i < len(sections) - 1 else rf"{section}\s*:\s*(.*)"
        else:
          
            pattern = rf"{section}:(.*)"

        match = re.search(pattern, soap_text, re.IGNORECASE | re.DOTALL)
        if match:
            content = match.group(1).strip()
            output[section] = {
                "word_count": count_words(content),
                "sentence_count": count_sentences(content)
            }
        else:
            output[section] = {
                "word_count": 0,
                "sentence_count": 0
            }

    print("\n Section Lengths:")
    for section, stats in output.items():
        print(f"  {section}: {stats['word_count']} words / {stats['sentence_count']} sentences")

# File Definitions
transcription_file = "session_transcription.txt"
audio_file = "session.mp3"
prompt1_file = "Prompts/Prompt1.txt"
prompt2_file = "Prompts/Prompt2a.txt"
prompt3_file = "Prompts/Prompt3.txt"
rubric_prompt = "Prompts/rubric_prompt_a.txt"
rubric_response_file = "rubric_response.txt"
exampleMSE_file = "ExampleMSE.txt"
hallucinationprompt_file = "Prompts/hallucinationprompt.txt"

# Checking for transcription
if os.path.exists(transcription_file):
   
    print("Loading transcription from file...")
    with open(transcription_file, "r") as file:
        transcribed_text = file.read()
else:
    transcribed_text = transcribe_audio(audio_file)["text"]
    with open(transcription_file, "w") as file:
        file.write(transcribed_text)

# Load the prompt and MSE files
with open(prompt1_file, "r") as file:
    prompt_template = file.read()

with open(prompt2_file, "r") as file:
    prompt2_template = file.read()

with open(prompt3_file, "r") as file:
    prompt3_template = file.read()

with open(rubric_prompt, "r") as file:
    rubric_prompt = file.read()

with open(exampleMSE_file, "r") as file:
    example_mse_content = file.read()

with open(hallucinationprompt_file, "r") as file:
    hallucinationprompt_template = file.read()

prompt1 = prompt_template.replace("{transcribed_text}", transcribed_text)
prompt1 = prompt1.replace("{Example_MSE}", example_mse_content)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

#Soap Note Generation
print("Generating first response...")
response1 = model.generate_content(
    prompt1
)

print(response1.text)
print("SOAP NOTE:", response1.text)
response1 = response1.text

#next time put these at the end of the output
evaluate_soap_structure(response1)
evaluate_section_lengths(response1)

hallucinationprompt = hallucinationprompt_template.replace("{transcribed_text}", transcribed_text)
hallucinationprompt = hallucinationprompt.replace("{response1}", response1)

hallucination_check = model.generate_content(
    hallucinationprompt
)
print("Hallucination Check:", hallucination_check.text)

prompt2 = prompt2_template.replace("{response1}", response1)

#MMSE Generation
print("Generating 2nd response...")
response2 = model.generate_content(
    prompt2
)

print("MSE:", response2.text)
response2 = response2.text

prompt3 = prompt3_template.replace("{response1}}", response1)
prompt3 = prompt3.replace("{response2}", response2)

#Risk Level Generation
print("Generating Thrid response:...")
response3 = model.generate_content(
prompt3
)

print("Risk Level: ", response3.text)
response3 = response3.text

#Rubric Evvaluation
print("\nEvaluating SOAP Note Clinically...\n")
rubricprompt = rubric_prompt.replace("{response1}", response1)
rubric_response = model.generate_content(rubricprompt)
rubric_text = rubric_response.text
print(rubric_text)

with open("soap_rubric_evaluation.txt", "w") as file:
    file.write(rubric_text)
