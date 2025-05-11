from flask import Flask
from app.lib import biblioteca_scriitori

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Aplicație Scriitori - Elena Guramba</h1>
    <ul>
        <li><a href="/mihail_sadoveanu">Mihail Sadoveanu</a></li>
        <li><a href="/descriere_mihail_sadoveanu">Descriere</a></li>
        <li><a href="/opere_mihail_sadoveanu">Opere</a></li>
    </ul>
    '''

@app.route('/mihail_sadoveanu')
def scriitor():
    return 'Mihail Sadoveanu - scriitor român'

@app.route('/descriere_mihail_sadoveanu')
def descriere():
    return biblioteca_scriitori.descriere_mihail_sadoveanu()

@app.route('/opere_mihail_sadoveanu')
def opere():
    return biblioteca_scriitori.opere_mihail_sadoveanu()
