import sys
from flask import Flask, url_for

from app.lib import feature

print('scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def acasa():
    ret = "<center><h1>Mari scriitori romani</h1></center>"
    ret += "<p>Descoperă universul fascinant al scriitorilor care au marcat literatura română și universală, dincolo de paginile cărților.</p>"
    ret += "<p><b>Agatha Christie<b>a fost una dintre cele mai renumite autoare de romane polițiste din toate timpurile, cunoscută pentru ingeniozitatea intrigilor și personajele sale emblematice, precum detectivul Hercule Poirot și Miss Marple. Supranumită „Regina crimei”, Christie a scris peste 60 de romane și numeroase piese de teatru, captivând cititori din întreaga lume cu mistere rafinate și răsturnări de situație neașteptate.</p>"
    ret += f"<a href={url_for('scriitor')}>Descoperiți mai multe despre viața și operele Agathei Christie</a>"
    return ret

@app.route("/Agathei Christie", methods=['GET'])
def scriitor():
    ret = "<center><h1>Agathei Christie</h1></center>"
    ret += "<h2>Agatha Christie – Maestra suspansului și regina literaturii polițiste</h2>"
    ret += "<p>Agatha Christie (1890–1976) a fost o scriitoare britanică de romane polițiste, recunoscută la nivel mondial ca una dintre cele mai influente autoare ale genului. Supranumită „Regina crimei”, ea a creat personaje memorabile precum Hercule Poirot și Miss Marple, devenite simboluri ale literaturii de mister. </p>"
    ret += "<p>A scris peste 60 de romane, 14 colecții de povestiri și cel mai longeviv spectacol de teatru din lume, „Capcana de șoareci”. Stilul său se remarcă prin intrigi bine construite, suspans constant și finaluri surprinzătoare. Moștenirea sa literară continuă să fascineze cititorii din toate generațiile.</p>"
    ret += "<p>Talentul Agathei Christie nu s-a limitat doar la romane — ea a avut un impact major și în teatru și film. Multe dintre lucrările sale au fost adaptate în ecranizări de succes, iar piesa „The Mousetrap” este jucată neîntrerupt pe scena londoneză din 1952. Stilul său clar, lipsit de violență grafică, dar plin de tensiune intelectuală, a făcut ca operele sale să fie accesibile și apreciate la scară largă. Prin contribuția ei, Christie a definit standardele romanului polițist clasic, lăsând o amprentă durabilă în literatura mondială.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Agatha Christie/Opera_reprezentativa", methods=['GET'])
def opera_rep():
    ret = "<center><h1>" +feature.opera_reprezentativa() + "</h1></center>"
    ret += "<p>Una dintre cele mai cunoscute și apreciate opere ale Agathei Christie este romanul „Crima din Orient Express” (Murder on the Orient Express), publicat în 1934. Această poveste fascinantă îl are în centrul acțiunii pe detectivul belgian Hercule Poirot, care investighează o crimă petrecută la bordul faimosului tren.</p>"
    ret += "<p>Printr-o intrigă inteligent construită, dialoguri tensionate și un final surprinzător, Christie reușește să țină cititorul în suspans până la ultima pagină. Romanul este considerat un exemplu clasic de mister „cu cameră închisă” și reflectă stilul distinctiv al autoarei – logică riguroasă, personaje bine conturate și o atmosferă elegantă, dar neliniștitoare.</p>"
    ret += "<p>„Crima din Orient Express” este un roman polițist în care detectivul Hercule Poirot investighează uciderea unui pasager la bordul trenului Orient Express, blocat de o furtună de zăpadă. Victima, un american pe nume Samuel Ratchett, este descoperit înjunghiat în compartimentul său, iar indiciile par să conducă în direcții contradictorii. </p>"
    ret += "<p>Pe măsură ce Poirot interoghează pasagerii, descoperă că toți par a avea legături ascunse cu o veche tragedie – răpirea și uciderea unei fetițe. Finalul dezvăluie un complot colectiv neașteptat, în care toți suspecții sunt, de fapt, complici la crimă.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('curent_lit')}>Curent literat</a><br>"
    ret += f"<a href={url_for('scriitor')}>Agatha Christie</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Agatha Christie/Curent_literar", methods=['GET'])
def curent_lit():
    ret = "<center><h1>"+ feature.curent_literar() + "</h1></center>"
    ret += "<p>Agatha Christie este reprezentanta de marcă a literaturii polițiste clasice, un gen care s-a dezvoltat în prima jumătate a secolului XX și face parte din curentul realist. </p>"
    ret += "<p>Scrierile sale se remarcă prin structură logică, investigarea rațională a crimei și o abordare obiectivă a faptelor, toate elemente caracteristice realismului. În același timp, Christie contribuie la epoca de aur a romanului detectivistic britanic, alături de autori ca Arthur Conan Doyle sau Dorothy L. Sayers, punând accent pe deducție, inteligență și mister, mai degrabă decât pe acțiune brutală sau detalii morbide.</p>"
    ret += "<p>Agatha Christie se încadrează în tradiția literaturii polițiste clasice, o ramură distinctă a realismului literar, care pune accent pe analiza logică a crimei și pe prezentarea obiectivă a evenimentelor. Operele ei reflectă trăsături clare ale realismului: redarea fidelă a mediului social, evidențierea comportamentului uman în fața dilemelor morale și structurarea narativă clară, lipsită de ambiguități.</p>"
    ret += "<p>Totodată, Christie este una dintre figurile centrale ale așa-numitei „Epoci de Aur” a romanului detectiv britanic (anii 1920–1940), perioadă în care misterul era construit ca un puzzle intelectual, destinat să fie rezolvat de cititor odată cu detectivul. În acest context, personajele ei celebre — precum Hercule Poirot și Miss Marple — nu rezolvă crimele prin violență, ci prin raționamente deductive și observație fină. </p>"
    ret += "<p>Spre deosebire de romanele polițiste moderne, care adesea explorează teme întunecate și metode științifice, stilul Agathei Christie rămâne unul elegant, cerebral și profund britanic, ancorat în valorile și convențiile sociale ale epocii sale.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"<a href={url_for('scriitor')}>Agatha Christie</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    sys.exit(pytest.main(["."]))
