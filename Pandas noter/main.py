import gradio as gr
import programmering.variabler_typer as variabler_typer
import programmering.conditionals as conditionals
import programmering.loops as loops
import programmering.functions as functions
import programmering.lists as lists
import programmering.strings as strings
import programmering.dict_tuple as dict_tuple
import programmering.files as files
import programmering.classes as classes

import matematik.pakker as pakker
import matematik.Differentialligninger as Differentialligninger
import matematik.Differentiabilitet as Differentiabilitet
import matematik.Egenværdier as Egenværdier
import matematik.Gradient as Gradient
import matematik.indre_produkt as indre_produkt
import matematik.jupyter_notebook as jupyter_notebook
import matematik.komplekse_tal as komplekse_tal
import matematik.lineære_afbildninger as lineære_afbildninger
import matematik.Matricer as Matricer
import matematik.Sympy as Sympy
import matematik.Taylor_Approksimationer as Taylor_Approksimationer
import matematik.Spektral as Spektral

import tema_pandas as pd
import tema_plots as pl
import chatbot

def create_app():
    with gr.Blocks() as app:
        gr.Markdown("# Python kommandoer - Fuldstændig liste")

        with gr.Tabs():
            with gr.Tab("👩‍💻 Programmering"):
                gr.Markdown("## 👩‍💻 Programmering")
                with gr.Accordion("Variabler og Typer", open=False):
                    variabler_typer.layout()
                with gr.Accordion("Conditionals", open=False):
                    conditionals.layout()
                with gr.Accordion("Loops", open=False):
                    loops.layout()
                with gr.Accordion("Functions", open=False):
                    functions.layout()
                with gr.Accordion("Lists", open=False):
                    lists.layout()
                with gr.Accordion("Strings", open=False):
                    strings.layout()
                with gr.Accordion("Dictionaries og Tuples", open=False):
                    dict_tuple.layout()
                with gr.Accordion("Files", open=False):
                    files.layout()
                with gr.Accordion("Classes", open=False):
                    classes.layout()
            with gr.Tab("🧮 Matematik"):
                gr.Markdown("## 🧮 Matematik")
                with gr.Accordion("Pakker", open=False):
                    pakker.layout()
                with gr.Accordion("Komplekse tal", open=False):
                    komplekse_tal.layout()
                with gr.Accordion("Matricer",open=False):
                    Matricer.layout()
                with gr.Accordion("Lineære Afbildninger",open=False):
                    lineære_afbildninger.layout()
                with gr.Accordion("Indre produkt og Norm",open=False):
                    indre_produkt.layout()
                with gr.Accordion("Egenværdier og Diagonalisering",open=False):
                    Egenværdier.layout()
                with gr.Accordion("Spektralsætningen, diagonalisering og Hermitiske matricer",open=False):
                    Spektral.layout()
                with gr.Accordion("Differentialligninger",open=False):
                    Differentialligninger.layout()
                with gr.Accordion("Taylor-Approksimationer",open=False):
                    Taylor_Approksimationer.layout()
                with gr.Accordion("Gradient",open=False):
                    Gradient.layout()
                with gr.Accordion("Differentiabilitet", open=False):
                    Differentiabilitet.layout()
            with gr.Tab("∑ Sympy"):
                Sympy.layout()
            with gr.Tab("📈 Plots"):
                pl.layout()
            with gr.Tab("🐼 Pandas"):
                pd.layout()
            with gr.Tab("📝 Markdown"):
                jupyter_notebook.layout()

        chatbot.layout()

    return app

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    app = create_app()
    app.launch(server_name="0.0.0.0", server_port=port, share=False)
