from flask import Flask, render_template, request
from app.libs.opere_rebreanu import gaseste_opera_reprezentativa, gaseste_curent_literar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    rezultat = ""
    if request.method == "POST":
        if request.form.get("opera"):
            rezultat = gaseste_opera_reprezentativa()
        elif request.form.get("curent"):
            rezultat = gaseste_curent_literar()
    return render_template("index.html", rezultat=rezultat)

if __name__ == "__main__":
    app.run(debug=True)


