from flask import Flask, render_template_string
from app.lib.helper import get_biografie, get_opere, get_citat

app = Flask(__name__)

TEMPLATE_BASE = """
<!doctype html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{{ titlu }}</title>
    <style>
        body { font-family: sans-serif; margin: 2em; background: #f0f2f5; color: #333; }
        h1 { color: #005577; }
        img { max-width: 100%%; height: auto; border-radius: 10px; margin-top: 10px; }
        .content { max-width: 800px; margin: auto; background: white; padding: 2em; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
        .back-btn { display: inline-block; margin-top: 20px; padding: 10px 20px; background: #005577; color: white; text-decoration: none; border-radius: 5px; }
        .back-btn:hover { background: #003f4f; }
    </style>
</head>
<body>
<div class="content">
    <h1>{{ titlu }}</h1>
    {{ continut | safe }}
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        TEMPLATE_BASE,
        titlu="Bine ai venit",
        continut=f"""
            <p>Acesta este un proiect dedicat lui <strong>Mihai Eminescu</strong>.</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/d/dc/Eminescu.jpg" alt="Mihai Eminescu" style="width: 300px; border-radius: 8px; margin-top: 10px;">
            <p>Vizitează rutele:
                <ul>
                    <li><a href="/eminescu/biografie">Biografie</a></li>
                    <li><a href="/eminescu/opere">Opere</a></li>
                    <li><a href="/eminescu/citat">Citat</a></li>
                </ul>
            </p>
        """
    )

@app.route('/eminescu/biografie')
def biografie():
    return render_template_string(
        TEMPLATE_BASE,
        titlu="Biografie – Mihai Eminescu",
        continut=f"""
            <p>{get_biografie()}</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/d/dc/Eminescu.jpg" alt="Mihai Eminescu" style="width: 300px; border-radius: 8px; margin-top: 10px;">
            <p><a class="back-btn" href="/">Înapoi la pagina principală</a></p>
        """
    )

@app.route('/eminescu/opere')
def opere():
    opere_html = ''.join(f"<li>{op}</li>" for op in get_opere())
    return render_template_string(
        TEMPLATE_BASE,
        titlu="Opere principale",
        continut=f"""
            <ul>{opere_html}</ul>
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/f2/Legenda_Luceaf%C4%95rului.png" alt="Opere Mihai Eminescu" style="width: 300px; border-radius: 8px; margin-top: 10px;">
            <p><a class="back-btn" href="/">Înapoi la pagina principală</a></p>
        """
    )

@app.route('/eminescu/citat')
def citat():
    return render_template_string(
        TEMPLATE_BASE,
        titlu="Citat celebru",
        continut=f"""
            <blockquote>{get_citat()}</blockquote>
            <p><a class="back-btn" href="/">Înapoi la pagina principală</a></p>
        """
    )

if __name__ == "__main__":
    app.run(debug=True, port=5050)
