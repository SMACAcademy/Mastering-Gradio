import gradio as gr
from transformers import pipeline

# Create the fill-mask pipeline
pipe = pipeline("fill-mask", model="medicalai/ClinicalBERT")

def predict_mask(text):
    # Use the pipeline to predict the masked word
    predictions = pipe(text)
    # Format the predictions to return only the text
    return [f"{pred['sequence']} (score: {pred['score']:.2f})" for pred in predictions]

# Create a Gradio interface
interface = gr.Interface(fn=predict_mask,
                         inputs="text",
                         outputs="text",
                         examples=[
                             ["The patient complained of [MASK] pain and fever."],
                             ["Due to a severe headache, the doctor prescribed [MASK]."],
                             ["After the accident, the patient's left [MASK] was fractured."]
                         ],
                         title="ClinicalBERT Fill-Mask Prediction",
                         description="Enter text with a [MASK] to see predictions for the masked word.")

# Launch the Gradio app
interface.launch()
