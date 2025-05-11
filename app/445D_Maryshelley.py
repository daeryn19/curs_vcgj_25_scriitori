from flask import Flask
import lib.biblioteca_scriitori  # Make sure this is the correct import path

app = Flask(__name__)

print('445D_scriitori')

@app.route("/", methods=['GET'])
def index():
    ret =  "<h1>Informații despre Mary Shelley - 445D</h1>"
    return ret

@app.route("/MaryShelley/", methods=['GET'])
def get_MaryShelley():
    ret = "<h1>Mary Shelley</h1>"
    ret += "Biografie: "
    ret += lib.biblioteca_scriitori.biografie_shelley()  # Call function from lib
    ret += "<br>"

    ret += "Lucrare celebră: "
    ret += lib.biblioteca_scriitori.lucrare_celebra_shelley()  # Call function from lib
    ret += "<br>"
    
    return ret

@app.route("/MaryShelley/biografie", methods=['GET'])
def ia_biografie_shelley():
    ret = lib.biblioteca_scriitori.biografie_shelley()  # Call function from lib
    return ret

@app.route("/MaryShelley/lucrare", methods=['GET'])
def ia_lucrare_shelley():
    ret = lib.biblioteca_scriitori.lucrare_celebra_shelley()  # Call function from lib
    return ret

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)

