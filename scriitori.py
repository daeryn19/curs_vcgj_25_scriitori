import sys
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def acasa():
    ret = "<center><h1>Scriitori Români Deosebiți</h1></center>"
    ret += "<p>Literatura română este marcată de talente valoroase, iar prin această secțiune ne propunem să aducem în prim-plan scriitori care au influențat profund cultura.</p>"
    ret += "<p>Un astfel de nume este <b>Rodica Ojog-Brașoveanu</b>, o autoare cu o contribuție semnificativă la literatura română contemporană.</p>"
    ret += f"<a href={url_for('scriitor')}>Află mai multe detalii despre Rodica Ojog-Brașoveanu</a>"
    return ret

@app.route("/Rodica_Ojog_Brasoveanu", methods=['GET'])
def scriitor():
    ret = "<center><h1>Rodica Ojog-Brașoveanu</h1></center>"
    ret += "<h2>O carieră literară remarcabilă în domeniul thriller-ului românesc</h2>"
    ret += "<p>Rodica Ojog-Brașoveanu (născută la 28 martie 1939 în România) a fost o autoare prolifică de romane polițiste și de suspans. A scris numeroase romane și nuvele care au captivat cititorii prin intrigile complexe și personaje interesante.</p>"
    ret += "<p>De-a lungul carierei sale, Ojog-Brașoveanu a reușit să creeze o atmosferă captivantă în care misterele și enigmele sunt la ordinea zilei, fiind o autoare de referință în literatura română contemporană de suspans.</p>"
    ret += "<h3>Informații suplimentare</h3>"
    ret += "<p>Rodica Ojog-Brașoveanu este cunoscută pentru seria de romane cu personajul principal pe nume 'Antonia', o femeie extrem de isteață, implicată în tot felul de aventuri periculoase, dar captivante.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativă</a><br>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasă</a>"
    return ret

@app.route("/Rodica_Ojog_Brasoveanu/Opera_reprezentativa", methods=['GET'])
def opera_rep():
    ret = "<center><h1>Opera reprezentativă: <i>Secretul celor trei</i></h1></center>"
    ret += "<p><i>Secretul celor trei</i> este una dintre cele mai populare lucrări ale Rodicăi Ojog-Brașoveanu. Acesta este un roman polițist care implică o serie de mistere legate de o dispariție misterioasă și o serie de evenimente care pun sub semnul întrebării moralitatea și intențiile celor implicați.</p>"
    ret += "<p>Romanul a avut un impact semnificativ asupra cititorilor români, fiind un exemplu al stilului său unic, care combină intriga psihologică cu acțiunea rapidă și suspansul.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('scriitor')}>Rodica Ojog-Brașoveanu</a><br>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasă</a>"
    return ret

@app.route("/Rodica_Ojog_Brasoveanu/Curent_literar", methods=['GET'])
def curent_lit():
    ret = "<center><h1>Curent literar: Thriller și Suspans</h1></center>"
    ret += "<p>Rodica Ojog-Brașoveanu este o reprezentantă de seamă a literaturii de suspans și thriller din România. În cadrul acestui curent literar, autoarea abordează teme precum misterul, conflictele psihologice ale personajelor, dar și explorarea adâncă a naturii umane în fața unor situații limite.</p>"
    ret += "<p>Thrillerul, ca și curent literar, se caracterizează prin tensiunea constantă, printr-o atmosferă de neliniște și incertitudine care pătrunde adânc în psihicul cititorului. Rodica Ojog-Brașoveanu a reușit să capteze aceste trăsături prin operele sale care sunt cu adevărat captivante și imprevizibile.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('scriitor')}>Rodica Ojog-Brașoveanu</a><br>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativă</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasă</a>"
    return ret

@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    sys.exit(pytest.main(["."]))

if __name__ == '__main__':
    app.run(debug=True)

