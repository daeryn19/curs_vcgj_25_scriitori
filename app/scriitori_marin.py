from flask import Flask
from lib.biblioteca_scriitori import viata_eminescu, opera_eminescu

app = Flask(__name__)

@app.route('/eminescu')
def index():
    return "Aceasta este pagina despre Mihai Eminescu."

@app.route('/eminescu/viata')
def viata():
    return viata_eminescu()

@app.route('/eminescu/opera')
def opera():
    return opera_eminescu()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
