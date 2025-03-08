import gradio as gr

from transformers import pipeline

pipe = pipeline("translation", model="medicalai/ClinicalBERT")

def predict(text):
  return pipe(text)[0]["translation_text"]

demo = gr.Interface(
  fn=predict,
  inputs='text',
  outputs='text',
)

demo.launch()