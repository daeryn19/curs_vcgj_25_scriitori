from flask import Flask, url_for
from app.libs.biblioteca_scriitori_opera import magnum_opus
from app.libs.biblioteca_scriitori_gen import genre

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    ret = "<h1>Victor Hugo - Scriitor</h1>"
    ret += f"<h3>Acest site este dedicat scriitorului Victor Hugo:</h3>"
    ret += f"<a href='{url_for('opera_literara')}'>Opera Principală</a><br>"
    ret += f"<a href='{url_for('gen_literar')}'>Gen Literar</a><br>"
    return ret

@app.route("/opera_literara", methods=["GET"])
def opera_literara():
    return f"<h1>Opera lui Victor Hugo</h1><p>{magnum_opus()}</p>"

@app.route("/gen_literar", methods=["GET"])
def gen_literar():
    return f"<h1>Genul literar al lui Victor Hugo</h1><p>{genre()}</p>"

if __name__ == "__main__":
    app.run(debug=True)
