from flask import Flask, url_for
from app.lib import biblioteca_scriitori_opera
from app.lib import biblioteca_scriitori_gen

print ('Scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1> Scriitori</h1>"

    # Adaug butoanele pentru paginile secundare
    ret += "<h3>Aceasta pagina este dedicata scriitorilor din toata lumea. Scriitorul ales de studentul Mihaila Adelin-Gabriel:</h3>"
    ret += f"<a href={url_for('scriitor')}>Tahereh Mafi</a><br>"
    ret += f"<a href={url_for('opera_literara')}>Tahereh Mafi Magnum Opus</a><br>"
    ret += f"<a href={url_for('gen_literar')}>Genul literar abordat de Tahereh Mafi</a><br>"

    return ret

@app.route("/scriitor", methods=['GET'])
def scriitor():
    ret = "<h1>Tahereh Mafi - Scriitor</h1>"
    ret += "<p>Tahereh Mafi este o autoare cunoscută pentru seria sa 'Shatter Me' și pentru stilul său unic de a scrie.</p>"
    ret += f"<a href={url_for('index')}>Scriitori</a><br>"
    ret += f"<a href={url_for('opera_literara')}>Tahereh Mafi Magnum Opus</a><br>"
    ret += f"<a href={url_for('gen_literar')}>Genul literar abordat de Tahereh Mafi</a><br>"

    return ret

@app.route("/scriitor/opera", methods=['GET'])
def opera_literara():
    ret = "<h1>Tahereh Mafi - </h1>" + biblioteca_scriitori_opera.magnum_opus()
    ret += "<p>Una dintre cele mai bune lucrări ale lui Tahereh Mafi este primul volum din seria 'Shatter Me'.</p>"
    ret += f"<a href={url_for('index')}>Scriitori</a><br>"
    ret += f"<a href={url_for('scriitor')}>Tahereh Mafi</a><br>"
    ret += f"<a href={url_for('gen_literar')}>Genul literar abordat de Tahereh Mafi</a><br>"
    return ret

@app.route("/scriitor/gen", methods=['GET'])
def gen_literar():
    ret = "<h1>Genul literar abordat de Tahereh Mafi</h1>" + biblioteca_scriitori_gen.genre()
    ret += "<p>Tahereh Mafi scrie în principal în genul distopic, fantezie și science fiction, explorând teme complexe despre putere, iubire și supraviețuire.</p>"
    ret += f"<a href={url_for('index')}>Scriitori</a><br>"
    ret += f"<a href={url_for('scriitor')}>Tahereh Mafi</a><br>"
    ret += f"<a href={url_for('opera_literara')}>Tahereh Mafi Magnum Opus</a><br>"
    return ret

@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
