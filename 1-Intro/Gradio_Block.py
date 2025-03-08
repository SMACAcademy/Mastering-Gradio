import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        name = gr.Textbox(label="Your Name")
        intensity = gr.Slider(minimum=1, maximum=10, label="Greeting Intensity")
    greet_button = gr.Button("Greet")
    output = gr.Textbox(label="Greeting Output", interactive=True)

    # Correct the lambda function to convert intensity to int
    greet_button.click(
        fn=lambda name, intensity: "Hello, " + name + "!" * int(intensity),
        inputs=[name, intensity],
        outputs=output
    )

demo.launch(share=True)
