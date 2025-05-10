from flask import Flask
from app.lib.helper import get_biografie, get_opere, get_citat

app = Flask(__name__)

@app.route('/')
def home():
    return "Bine ai venit! Accesează /arghezi, /biografie, /opere, /citat"

@app.route('/arghezi')
def scriitor():
    return "Ai selectat scriitorul: Tudor Arghezi"

@app.route('/biografie')
def biografie():
    return get_biografie()

@app.route('/opere')
def opere():
    return "<br>".join(get_opere())

@app.route('/citat')
def citat():
    return get_citat()

if __name__ == '__main__':
    app.run(debug=True)
