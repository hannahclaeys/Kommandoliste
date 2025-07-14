import gradio as gr
import pandas as pd
from pygments import highlight as pygment_highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

kommandoer = pd.read_csv("data/kommandoer.csv")

def highlight(code, query=None):
    formatter = HtmlFormatter(style="monokai", linenos=False)
    css = formatter.get_style_defs('.highlight')
    highlighted = pygment_highlight(code, PythonLexer(), formatter)
    if query:
        highlighted = highlighted.replace(query, f"<mark>{query}</mark>")
    return f"<style>{css}</style>{highlighted}"

def chatbot_response(history, message):
    query = message.lower()

    matches = kommandoer[
        kommandoer["Beskrivelse"].str.lower().str.contains(query, na=False) |
        kommandoer["Kode"].str.lower().str.contains(query, na=False)
    ]

    if not matches.empty:
        svar = """
        <div style='max-height: 600px; overflow-y: auto; padding-right: 10px; display: flex; flex-direction: column; gap: 1em;'>
        """
        grupperet = matches.groupby("Kategori")
        for kategori, gruppe in grupperet:
            svar += f"""
            <div style='background-color: #3b3b3b; padding: 8px 12px; border-left: 4px solid #0af; border-radius: 6px; font-weight: bold; color: #fff;'>
                {kategori}
            </div>
            """
            for _, row in gruppe.iterrows():
                kode = row['Kode'].replace("<", "&lt;").replace(">", "&gt;")
                svar += f"""
                <div style=\"border: 1px solid #444; border-radius: 8px; padding: 10px;\">
                    <div style=\"font-weight: bold; margin-bottom: 4px;\">🔹 {highlight(row['Beskrivelse'], query)}</div>
                    <pre style=\"text-align: left;\"><code style=\"font-family: 'Courier New', monospace;\">{kode}</code></pre>
                </div>
                """
        svar += "</div>"
    else:
        svar = "<p>❌ Jeg fandt ingen relevante kommandoer.</p>"

    return svar, ""

def layout():
    with gr.Blocks() as demo:
        gr.HTML("""
        <style>
        mark {
            background-color: rgba(255, 255, 0, 0.25);
            padding: 2px 4px;
            border-radius: 3px;
        }
        </style>
        """)

        with gr.Row():
            with gr.Column(scale=3, min_width=600):
                gr.Markdown("### 💬 SØG I ALLE KOMMANDOER HER")
                output = gr.HTML()
                msg = gr.Textbox(label="Søgfunktion", placeholder="Fx 'drop', 'csv'")
                state = gr.State([])

                msg.submit(fn=chatbot_response, inputs=[state, msg], outputs=[output, msg])

    return demo