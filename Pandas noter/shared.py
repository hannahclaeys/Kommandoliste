import gradio as gr

with gr.Blocks() as app:
    gr.Markdown("# 🤓 Python kommandoer - Fuldstændig liste 🤓")
    gr.Code("ODE = sp.diff(f(t), t, 2) - 6*sp.diff(f(t), t) + 9*f(t)")

app.launch()