import gradio as gr
import pandas as pd
from pygments import highlight as pygment_highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

kommandoer = pd.read_csv("data/kommandoer.csv")
kommandoer = kommandoer[kommandoer["Kategori"] == "Lineær Afbildning"]

def lav_html_tabel(df):
    formatter = HtmlFormatter(style="monokai", noclasses=True)  # Brug farver direkte i HTML

    html = f"""
    <style>
        .scroll-table {{
            max-height: 500px;
            overflow: auto;
            border: 1px solid #555;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #333;
            padding: 8px;
            text-align: left;
            vertical-align: top;
        }}
        th {{
            background-color: #111;
            color: #fff;
        }}
        tr:nth-child(even) {{
            background-color: #2a2a2a;
        }}
        tr:nth-child(odd) {{
            background-color: #1f1f1f;
        }}

        .scroll-table::-webkit-scrollbar {{
            width: 12px;
            height: 12px;
        }}
        .scroll-table::-webkit-scrollbar-track {{
            background: #1a1a1a;
        }}
        .scroll-table::-webkit-scrollbar-thumb {{
            background-color: #555;
            border-radius: 6px;
            border: 3px solid #1a1a1a;
        }}
        .scroll-table::-webkit-scrollbar-thumb:hover {{
            background-color: #888;
        }}
    </style>
    <div class="scroll-table">
    <table>
        <thead>
            <tr><th>Beskrivelse</th><th>Kode</th></tr>
        </thead>
        <tbody>
    """

    for _, row in df.iterrows():
        beskrivelse = row["Beskrivelse"]
        kode = row["Kode"].replace("<", "&lt;").replace(">", "&gt;")
        # Brug pygments til at farvelægge koden
        farvet_kode = pygment_highlight(kode, PythonLexer(), formatter)
        html += f"<tr><td>{beskrivelse}</td><td>{farvet_kode}</td></tr>"

    html += "</tbody></table></div>"
    return html

def søg(query):
    # Lav en maske der matcher på både Beskrivelse og Kode
    mask = (
        kommandoer["Beskrivelse"].str.contains(query, case=False, na=False)
        | kommandoer["Kode"].str.contains(query, case=False, na=False)
    )
    return lav_html_tabel(kommandoer[mask][["Beskrivelse", "Kode"]])

def layout():
    with gr.Blocks() as ui:
        gr.Markdown("## 🧮 Lineær Afbildning")
        søgefelt = gr.Textbox(label="Søgefunktion", placeholder="Søg: fx 'drop', 'csv'...")
        html_visning = gr.HTML(value=lav_html_tabel(kommandoer))

        søgefelt.change(fn=søg, inputs=søgefelt, outputs=html_visning)

    return ui

