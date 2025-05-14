"""
Aplicație Flask pentru gestionarea informațiilor despre Victor Hugo.
"""

from flask import Flask, url_for
from app.libs.biblioteca_scriitori_opera import magnum_opus
from app.libs.biblioteca_scriitori_gen import genre

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Pagină principală care afișează informații despre scriitor.
    """
    ret = "<h1> Scriitori</h1>"
    ret += "<h3>Aceasta pagina este dedicata scriitorului Victor Hugo:</h3>"
    ret += '<a href="{}">Victor Hugo</a><br>'.format(url_for('scriitor'))
    ret += '<a href="{}">Opera principală a lui Victor Hugo</a><br>'.format(url_for('opera_literara'))
    ret += '<a href="{}">Genul literar al lui Victor Hugo</a><br>'.format(url_for('gen_literar'))
    return ret

@app.route("/scriitor", methods=["GET"])
def scriitor():
    """
    Informații despre scriitor.
    """
    return "<h1>Victor Hugo - Scriitor</h1><p>Victor Hugo a fost un poet, romancier și dramaturg francez, lider al romantismului în Franța.</p>"

@app.route("/scriitor/opera", methods=["GET"])
def opera_literara():
    """
    Informații despre opera principală a scriitorului.
    """
    return f"<h1>Victor Hugo - Magnum Opus</h1><p>{magnum_opus()}</p>"

@app.route("/scriitor/gen", methods=["GET"])
def gen_literar():
    """
    Informații despre genul literar al scriitorului.
    """
    return f"<h1>Genul literar abordat de Victor Hugo</h1><p>{genre()}</p>"

