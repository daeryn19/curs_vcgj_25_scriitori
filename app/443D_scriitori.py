
import sys
from flask import Flask, url_for
from app.libs import biblioteca_scriitori

app = Flask(__name__)

@app.route("/")
def homepage():
    return f"""
    <h1>Biblioteca scriitorilor – Burlacu Andreea</h1>
    <ul>
        <li><a href="{url_for('pagina_victor_hugo')}">Victor Hugo</a></li>
    </ul>
    """

@app.route("/victor-hugo")
def pagina_victor_hugo():
    return f"""
    <h1>Victor Hugo</h1>
    <p><a href="{url_for('descriere_victor')}">Află cine a fost Victor Hugo</a></p>
    <p><a href="{url_for('opere_victor')}">Vezi operele sale</a></p>
    <p><a href="{url_for('homepage')}">Înapoi la pagina principală</a></p>
    """

@app.route("/victor-hugo/despre")
def descriere_victor():
    descriere = biblioteca_scriitori.descriere_victor_hugo()
    return f"""
    <h2>Descriere</h2>
    <p>{descriere}</p>
    <p><a href="{url_for('pagina_victor_hugo')}">Înapoi la Victor Hugo</a></p>
    """

@app.route("/victor-hugo/opere")
def opere_victor():
    opere = biblioteca_scriitori.opere_victor_hugo()
    return f"""
    <h2>Opere Reprezentative</h2>
    <p>{opere}</p>
    <p><a href="{url_for('pagina_victor_hugo')}">Înapoi la Victor Hugo</a></p>
    """

@app.cli.command()
def test():
    """
    Rulare teste unitare cu Pytest
    """
    import pytest
    sys.exit(pytest.main(["."]))

