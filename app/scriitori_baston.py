from flask import Flask
from lib.biblioteca_scriitori import viata_rebreanu, opera_rebreanu

app = Flask(__name__)

@app.route('/rebreanu')
def index():
    return "Aceasta este pagina despre Liviu Rebreanu."

@app.route('/rebreanu/viata')
def viata():
    return viata_rebreanu()

@app.route('/rebreanu/opera')
def opera():
    return opera_rebreanu()

if __name__ == "__main__":
    app.run(debug=True)
