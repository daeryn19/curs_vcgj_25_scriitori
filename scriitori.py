import sys
from flask import Flask, url_for

from app.libs import feature

print('scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def acasa():
    ret = "<center><h1>Mari scriitori universali</h1></center>"
    ret += "<p>Această platformă își propune să valorifice și să promoveze contribuția esențială a scriitorilor la patrimoniul literar universal. Printre cei mai influenți creatori ai secolului XX se numără <b>J. R. R. Tolkien</b>, autorul care a definit literatura fantasy modernă prin capodoperele sale.</p>"
    ret += "<p>În această secțiune, ne vom opri asupra vieții, operei și moștenirii literare a lui Tolkien, explorând universul fascinant al Pământului de Mijloc.</p>"
    ret += f"<a href={url_for('scriitor')}>Află mai multe detalii despre scriitorul J. R. R. Tolkien</a>"
    return ret

@app.route("/Tolkien", methods=['GET'])
def scriitor():
    ret = "<center><h1>J. R. R. Tolkien</h1></center>"
    ret += "<h2>Creatorul Pământului de Mijloc</h2>"
    ret += "<p>John Ronald Reuel Tolkien (1892–1973) a fost un filolog, profesor universitar și autor britanic, cunoscut mai ales pentru trilogia „Stăpânul Inelelor”, predecesorul acesteia „Hobbitul” și mitologia amplă dezvoltată în „Silmarillion”.</p>"
    ret += "<p>Tolkien a fost profesor de limbă și literatură engleză veche la Universitatea Oxford, iar pasiunea sa pentru limbi inventate și mitologie a stat la baza lumii complexe și coerente din cărțile sale. A fost profund influențat de mitologia nordică, anglo-saxonă și celtică.</p>"
    ret += "<p>Opera sa a influențat profund genul fantasy, stabilind standarde pentru construcția de lumi ficționale, arcuri narative epice și personaje mitologice. A fost numit „părintele literaturii fantasy moderne”.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Operă reprezentativă</a><br>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasă</a>"
    return ret

@app.route("/Tolkien/Opera_reprezentativa", methods=['GET'])
def opera_rep():
    ret = "<center><h1>" + feature.gaseste_opera_reprezentativa() + "</h1></center>"
    ret += "<p>„Stăpânul Inelelor” este considerată opera majoră a lui Tolkien și una dintre cele mai importante lucrări din literatura fantasy. Publicată între 1954 și 1955 în trei volume, povestea urmărește lupta dintre bine și rău într-o lume fantastică, Pământul de Mijloc, unde un inel puternic trebuie distrus pentru a opri tirania lordului întunecat Sauron.</p>"
    ret += "<p>Romanul explorează teme universale precum prietenia, sacrificiul, coruperea puterii, destinul și speranța. Tolkien a creat o mitologie completă cu limbi proprii, istorie, geografie și rase (elfi, pitici, orci, oameni etc.).</p>"
    ret += "<p>„Stăpânul Inelelor” a avut un impact uriaș în cultura populară, fiind adaptată în filme, jocuri și benzi desenate, devenind un simbol global al genului fantasy.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('scriitor')}>J. R. R. Tolkien</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasă</a>"
    return ret

@app.route("/Tolkien/Curent_literar", methods=['GET'])
def curent_lit():
    ret = "<center><h1>" + feature.gaseste_curent_literar() + "</h1></center>"
    ret += "<p>Literatura fantasy este un gen care presupune existența unor lumi imaginare, în care magia, creaturile mitologice și forțele supranaturale sunt elemente centrale. Tolkien este considerat pionierul acestui gen în forma sa modernă.</p>"
    ret += "<p>Caracteristicile definitorii ale fantasy-ului tolkienian includ: construcția de lumi coerente (world-building), mitologii proprii, limbi inventate, tipologii morale clare și influențe profunde din mitologia nordică și europeană clasică.</p>"
    ret += "<p>Opera sa stă la baza unui curent literar și artistic numit „high fantasy” (fantasy înalt), în care povestea are un caracter epic și simbolic, și este plasată într-un univers detaliat, total separat de lumea reală.</p>"
    ret += "<p>Tolkien a reușit nu doar să creeze o poveste, ci un întreg univers alternativ, care a inspirat generații de autori și cititori, de la literatura fantasy la cinematografie și cultura geek.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Operă reprezentativă</a><br>"
    ret += f"<a href={url_for('scriitor')}>J. R. R. Tolkien</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasă</a>"
    return ret

@app.cli.command()
def test():
    """Rulare 'unit tests' din aplicația Flask"""
    import pytest
    sys.exit(pytest.main(["."]))