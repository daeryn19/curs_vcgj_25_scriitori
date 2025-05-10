import sys
from flask import Flask, url_for
from app.libs import biblioteca_scriitori

app = Flask(__name__)

@app.route("/")
def homepage():
    return f"""
    <h1>Biblioteca Scriitorilor</h1>
    <ul>
        <li><a href="{url_for('pagina_dmitry_glukhovsky')}">Dmitry Glukhovsky</a></li>
    </ul>
    """

@app.route("/dmitry-glukhovsky")
def pagina_dmitry_glukhovsky():
    return f"""
    <h1>Dmitry Glukhovsky</h1>
    <p><a href="{url_for('descriere_dmitry')}">Află cine este Dmitry Glukhovsky</a></p>
    <p><a href="{url_for('opere_dmitry')}">Vezi operele sale</a></p>
    <p><a href="{url_for('homepage')}">Înapoi la pagina principală</a></p>
    """

@app.route("/dmitry-glukhovsky/despre")
def descriere_dmitry():
    descriere = biblioteca_scriitori.descriere_dmitry_glukhovsky()
    return f"""
    <h2>Descriere</h2>
    <p>{descriere}</p>
    <p><a href="{url_for('pagina_dmitry_glukhovsky')}">Înapoi la Dmitry Glukhovsky</a></p>
    """

@app.route("/dmitry-glukhovsky/opere")
def opere_dmitry():
    opere = biblioteca_scriitori.opere_dmitry_glukhovsky()
    return f"""
    <h2>Opere Reprezentative</h2>
    <p>{opere}</p>
    <p><a href="{url_for('pagina_dmitry_glukhovsky')}">Înapoi la Dmitry Glukhovsky</a></p>
    """

@app.cli.command()
def test():
    """
    Rulare teste unitare cu Pytest
    """
    import pytest
    sys.exit(pytest.main(["."]))
