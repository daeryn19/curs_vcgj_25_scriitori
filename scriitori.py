import sys
from flask import Flask, url_for

from app.libs import feature

print('scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def acasa():
    ret = "<center><h1>Scriitori internationali</h1></center>"
    ret += "<p>Această platformă își propune să pună în lumină contribuția esențială a scriitorilor internationali, asemenea modului în care Ruta Sepetys aduce la suprafață povești uitate și voci tăcute ale trecutului.</p>"
    ret += "<p>În aceasta sectiune, ne vom opri asupra uneia dintre personalitatile de seama ale literaturii universale: <b>Ruta Sepetys</b>.  În calitate de autoare a scris bestselleruri internaționale ce au apărut pe lista New York Times și este câștigătoare a medaliei Carnegie și a Premiului Josette Frank pentru ficțiune.</p>"
    ret += f"<a href={url_for('scriitor')}>Aflati mai multe detalii despre scriitorul Ruta Sepetys</a>"
    return ret

@app.route("/Ruta_Sepetys", methods=['GET'])
def scriitor():
    ret = "<center><h1>Ruta Sepetys</h1></center>"
    ret += "<h2>O viata dedicata literaturii de ficțiune istorică bazată pe povești uitate</h2>"
    ret += "<p>Ruta Sepetys (n 1976) o autoare americană de origine lituaniană, cunoscută pentru romanele sale istorice dedicate adolescenților și tinerilor adulți. </p>"
    ret += "<p>Scrie despre momente mai puțin cunoscute ale istoriei, punând accent pe vocea celor marginalizați sau uitați.</p>"
    ret += "<p>Pe măsură ce regimurile comuniste se prăbușesc în Europa în 1989, Sfârșitul șoaptelor: Decembrie 1989 (I Must Betray You), publicat în 2022, descrie lumea lui Cristian Florescu, un elev de șaptesprezece ani din București, în vremea României lui Nicolae Ceaușescu. El trebuie să decidă dacă să fie informator sau să reziste regimului. Această carte a câștigat și Premiul Yoto Carnegie Shadower pentru scris în 2023.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Ruta_Sepetys/Opera_reprezentativa", methods=['GET'])
def opera_rep():
    ret = "<center><h1>" +feature.gaseste_opera_reprezentativa() + "</h1></center>"
    ret += "<p>„Sfârșitul șoaptelor” (2022) Cartea urmărește povestea lui Cristian Florescu, un adolescent român de 17 ani, care trăiește în dictatura comunistă a lui Ceaușescu. </p>"
    ret += "<p>Viața lui este schimbată radical când este forțat să devină informator al Securității, poliția secretă a regimului.Cristian trebuie să decidă dacă se supune sistemului sau îl înfruntă, riscând viața lui și a celor dragi.</p>"
    ret += "<p>Teme principale sunt: Trădarea vs. loialitatea – Cristian este prins între dorința de a-și proteja familia și lupta pentru adevăr. Frică și control social – Regimul controlează fiecare aspect al vieții: de la alimente și electricitate, până la libertatea de exprimare. Puterea adevărului și a rezistenței – Chiar și în cele mai întunecate regimuri, speranța și curajul pot supraviețui.</p>"
    ret += "<p>Se bazează pe documentare riguroasă și interviuri reale cu români care au trăit sub dictatura comunistă.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('curent_lit')}>Curent literat</a><br>"
    ret += f"<a href={url_for('scriitor')}>Ruta Sepetys</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Ruta_Sepetys/Curent_literar", methods=['GET'])
def curent_lit():
    ret = "<center><h1>"+ feature.gaseste_curent_literar() + "</h1></center>"
    ret += "<p>Ficțiunea istorică este un gen literar în care autorii creează povești ficționale ce se desfășoară în contexte istorice reale.</p>"
    ret += "<p>Caracteristici ale ficțiunii istorice:</p>"
    ret += "<p>Contextul istoric real: Evenimentele din poveste sunt plasate într-o perioadă istorică reală, cum ar fi Evul Mediu, Renașterea, sau perioada celui de-al Doilea Război Mondial. </p>"
    ret += "<p>Personaje reale și fictive: Personajele ficționale pot interacționa cu figuri istorice reale. De exemplu, o poveste poate explora viața unui personaj real, dar poate include și personaje inventate care influențează evenimentele din acea perioadă.</p>"
    ret += "<p>Documentare și cercetare: Un aspect esențial al ficțiunii istorice este cercetarea temeinică. Autorii trebuie să studieze în profunzime istoria pentru a crea o atmosferă autentică, în ceea ce privește obiceiurile, comportamentele sociale și structurile politice din acea perioadă.</p>"
    ret += "<p>Fuzionarea faptului cu ficțiunea: Deși ficțiunea istorică poate include fapte reale, autorii pot adăuga elemente imaginare pentru a da sens sau adâncire poveștilor. </p>"
    ret += "<p>Sepetys este considerată una dintre cele mai importante autoare de ficțiune istorică pentru tineri din prezent, fiind apreciată pentru abilitatea sa de a aduce la lumină povești dureroase și neștiute, dar esențiale pentru înțelegerea istoriei secolului 20.</p>"
    ret += "<p>Este un exemplu clar de ficțiune istorică, deoarece: Acțiunea are loc într-un context real – România anului 1989, în ultimele luni ale regimului Ceaușescu. Personajele sunt ficționale, dar inspirate din realitate. Evenimentele istorice (foametea, cenzura, revoluția) sunt prezentate cu acuratețe documentară.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"<a href={url_for('scriitor')}>Ruta Sepetys</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret
@app.cli.command()
def test():
    """
    Rulare 'unit test'
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    sys.exit(pytest.main(["."]))
