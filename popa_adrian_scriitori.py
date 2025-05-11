from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.carti import get_carti
from app.lib.curent_literar import get_curent_literar

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Tema: Autori</h1>
	<p>Acest site oferă informații esențiale despre mari autori ai literaturii universale. Momentan este prezentat John Steinbeck.</p>
        <p><a href="/John_Steinbeck">John Steinbeck</a></p>
    '''

@app.route("/John_Steinbeck")
def John_Steinbeck():
    return '''
        <h1>John_Steinbeck</h1>
        <p><a href="/John_Steinbeck/descriere">Descriere generala</a></p>
        <p><a href="/John_Steinbeck/carti">Cărți reprezentative</a></p>
	<p><a href="/John_Steinbeck/curent_literar">Curent Literar</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/John_Steinbeck/descriere")
def descriere():
    text = get_descriere()
    return f'''
        <h1>Descrierea John Steinbeck</h1>
        <p>{text}</p>
        <p><a href="/John_Steinbeck">Înapoi la John_Steinbeck</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/John_Steinbeck/carti")
def carti():
    text = get_carti()
    return f'''
        <h1>Carti John Steinbeck</h1>
        <p>{text}</p>
        <p><a href="/John_Steinbeck">Înapoi la John_Steinbeck</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

@app.route("/John_Steinbeck/curent_literar")
def curent_literar():
    text = get_curent_literar()
    return f'''
        <h1>Curent Literar</h1>
        <p>{text}</p>
        <p><a href="/John_Steinbeck">Înapoi la John_Steinbeck</a></p>
        <p><a href="/">Înapoi la pagina principală</a></p>
    '''

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)