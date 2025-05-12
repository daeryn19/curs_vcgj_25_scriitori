import sys
from flask import Flask, url_for

from app.lib import biblioteca

print('scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def acasa():
    ret = "<center><h1>scriitori</h1></center>"
    ret += f"<a href={url_for('scriitor')}>William Shakespeare</a>"
    return ret

@app.route("/William Shakespear", methods=['GET'])
def scriitor():
    ret = "<center><h1>William Shakespear</h1></center>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/William Shakespear/Opera_reprezentativa", methods=['GET'])
def opera_rep():
    ret = "<center><h1>" +biblioteca.opera_reprezentativa() + "</h1></center>"
    ret += f"<a href={url_for('curent_lit')}>Curent literat</a><br>"
    ret += f"<a href={url_for('scriitor')}>Ioan Slavici</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/William Shakespear/Curent_literar", methods=['GET'])
def curent_lit():
    ret = "<center><h1>"+ biblioteca.curent_literar() + "</h1></center>"
    ret += f"<a href={url_for('scriitor')}>Ioan Slavici</a><br>"
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
