import sys
from flask import Flask, url_for

from app.libs import feature

print('scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def acasa():
    ret = "<h1>SCRIITORI</h1>"
    ret += f"Scriitor: <a href={url_for('scriitor')}>Ioan Slavici</a>"
    return ret

@app.route("/Ioan_Slavici", methods=['GET'])
def scriitor():
    ret = "<h1>Ioan Slavici</h1>"
    ret += f"Opera reprezentativa: <a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"Curent literar: <a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Ioan_Slavici/Opera_reprezentativa", methods=['GET'])
def opera_rep():
    ret = "<h1>" +feature.gaseste_opera_reprezentativa() + "</h1>"
    ret += f"Curent literar: <a href={url_for('curent_lit')}>Curent literat</a><br>"
    ret += f"Scriitor: <a href={url_for('scriitor')}>Ioan Slavici</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Ioan_Slavici/Curent_literar", methods=['GET'])
def curent_lit():
    ret = "<h1>"+ feature.gaseste_curent_literar() + "</h1>"
    ret += f"Opera reprezentativa: <a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"Scriitor: <a href={url_for('scriitor')}>Ioan Slavici</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    sys.exit(pytest.main(["."]))
