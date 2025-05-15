
# Notes on Prompt 1
speaker diarization appears adequate

next prompt, use a paragraph format with 3-4 sentences per section, with only 1 to 2 direct quotes per note section. 

Factors to include in objective are: speech, tone, affect, appearance, perceived mood

Assessment should start with patient is an (age) year old (gender) presenting for (symptoms or diagnosis) and include observations on how the patient is doing with engagement in therapy and adherence to treatment plan. Assessment should also provide a biopsychosocial evaluation of the patient that is overarching the entire therapeutic relationship with the patient. It is to be adapted over time as the patient changes in therapy. 

- Give definitaion on the biopsychosocial model 
The biopsychosocial model in clinical psychotherapy is a comprehensive framework that examines how mental health conditions are the result of complex interactions between biological, psychological, and social factors. Rather than focusing solely on symptoms or a single cause, this model emphasizes the importance of considering genetic predispositions, neurochemical imbalances, cognitive patterns, emotional regulation, interpersonal relationships, cultural influences, and environmental stressors when assessing and treating a client. The aim is to develop holistic, individualized treatment plans that integrate multiple domains of a person’s life to support meaningful and sustainable change.

MSE should be more brief, does not require full sentences

- Give the rubric evaluation prompt more guidance on how to grade responses. Rubric based grading is not informative, the model hits a ceiling of 24/24. 

# Notes on Prompt 2
still hits a ceiling with the grading rubric
 
 paragraph styling is better, reads more natural, however the quoted text is now longer, albeit its only one quote. LLM no longer writes like a technican "pt states...pt states...pt states..."

 Noticing some grammatical errors, inconsistencies. 

 The assessment setion is markedly improved; the biopsychosocial aspects are adequate but lack some readability. Adding an example text of the BSS model would likely help. 
 There seems to be two elements needed to produce helpful instruction, background information (explainer) and an example. 

 Using a golden dataset along with ground-truths is clearly needed. 

 treatment recommendations between prompts were different, however both responses are clinically relevant. Further guidance would need to be given around perferrred theoretical orientation and tx preferences to better guide the response generation. 

 Both word count and sentence totals is down; more concise answers. 

 Model hallucinated pt's age?

 MSE much better, more aligned with typical MSE's

 Risk could be lowered to no risk, rather than low. Should give model that explicit option, however some clincians do not like to give a no risk because "there's theoretically always a chance"

 Based on my inputs for the grading rubric, I think this output grade is accurate; more detail and most likely examples, need to be included for the rubric to have a proper floor and ceiling to grade against. 

 **I tried re-running the first prompt with the updated rubric (see Responses/SOAP Output/Response 3.txt) and it produced a grade of 19/24. So the basic grading technique of the rubric is validated (I'm not always hitting a ceiling).

I focused entirely on the verbal/clinical inputs and outputs and in future iterations, would focus more on changing parameteres for the LLM. Assuming Temp of .2-.3,  Top-P of .95, and Top-K of 30-40 is the standard starting point, I would adjust to 0 or .1, .90, and K of 10-20 and experiment with the outputs.

