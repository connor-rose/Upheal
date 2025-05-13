# Descriptive Statistics for SOAP Note
- section length

# Evaluation Methods
First evaluation is if all soap sections are present. Simple example of a concret heuristic check

## Trying to Evaluate for halluciantions
### First prompt
-----////------
Below is a psychotherapy session transcript followed by a SOAP note generated from it.
Your task is to identify **any statements or content in the SOAP note** that are **not supported by or mentioned in the transcript**. 
Be strict — even if something might be inferred, only consider it supported if it is directly stated or clearly implied in the transcript.
Respond with a list of potential hallucinated or unsupported statements. If everything in the SOAP note is consistent with the transcript, say "No hallucinations found."
Transcript:
\"\"\"{transcribed_text}\"\"\"
SOAP Note:
\"\"\"{response1}\"\"\"
-----////------

- First attempt at checking for hallucinations in the machine produced an evaluation of hallucantion symptoms present by the patient. 

### Second prompt to correct for this:
----////----
Below is a psychotherapy session transcript followed by a SOAP note generated from it.
Your task is to identify **any statements or content in the SOAP note** that are **not supported by or mentioned in the transcript**. 
Be strict — even if something might be inferred, only consider it supported if it is directly stated or clearly implied in the transcript.
Respond with a list of potential hallucinated or unsupported statements. If everything in the SOAP note is consistent with the transcript, say "No hallucinations found."
These references to *hallucination* are statements made by the LLM that are not supported by the data in the transcript. This does not refer to the clinical symptom of hallucinating that may or may not be experienced by the patient. This evaluation is focused on the LLM response, not on the patient symptoms. 
Transcript:
\"\"\"{transcribed_text}\"\"\"
SOAP Note:
\"\"\"{response1}\"\"\"
----////----
This resulted in the LLM highilghting any inference or assumption as hallucination, as well as any phrasing in the transcript that came from the video reviewer. I need to add a line in the prompt to not evaluate the transcript for hallucinations. 
