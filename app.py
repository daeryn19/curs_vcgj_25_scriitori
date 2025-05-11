from flask import Flask, render_template, redirect
from lib.biblioteca_scriitori import data_nasterii, data_mortii, opere

app = Flask(__name__)

@app.route("/frankherbert")
def info():
    return render_template("index.html")

@app.route("/")
def home():
    return redirect("/frankherbert")
    
@app.route("/frankherbert/opere")
def lucrari():
    return render_template("opere.html", opere=opere())

@app.route("/frankherbert/nastere")
def nastere():
    return render_template("nastere.html", nastere=data_nasterii(), moarte=data_mortii())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

