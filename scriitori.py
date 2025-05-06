import sys

from flask import Flask, url_for

from app.libs import biblioteca_scriitori


print('scriitori')


app = Flask(__name__)


@app.route("/", methods=['GET'])
def acasa():
    ret = "<h1>scriitori</h1>"
    ret += f"<a href={url_for('scriitor')}>Ion Luca Caragiale</a>"
    return ret

@app.route ("/Ion_Luca_Caragiale", methods=['GET'])
def scriitor():
    ret = "<h1>Ion Luca Caragiale</h1>"
    ret += f"<a href={url_for('opera_reprezentativa')}>Opera reprezentativa</a>"
    ret += f"<a href={url_for('curent_literar')}>Curent literar</a>"
    ret += f"<a href={url_for('acasa')}>Pagina principala</a>"
    return ret

@app.route ("/Ion_Luca_Caragiale/Opera_reprezentativa", methods=['GET'])
def opera_reprezentativa():
    ret = "<h1>"+biblioteca_scriitori.opera_reprezentativa_Caragiale()+"</h1>"
    ret += f"<a href={url_for('scriitor')}>Ion Luca Caragiale</a>"
    ret += f"<a href={url_for('curent_literar')}>Curent literar</a>"
    ret += f"<a href={url_for('acasa')}>Pagina principala</a>"
    return ret


@app.route ("/Ion_Luca_Caragiale/Curent_literar", methods=['GET'])
def curent_literar():
    ret = "<h1>"+biblioteca_scriitori.curent_literar_Caragiale()+"</h1>"
    ret += f"<a href={url_for('opera_reprezentativa')}>Opera reprezentativa</a>"
    ret += f"<a href={url_for('scriitor')}>Ion Luca Caragiale</a>"
    ret += f"<a href={url_for('acasa')}>Pagina principala</a>"
    return ret


@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
