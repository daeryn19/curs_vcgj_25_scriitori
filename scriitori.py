import sys
from flask import Flask, url_for

from app.libs import feature

print('scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def acasa():
    ret = "<center><h1>Mari scriitori romani</h1></center>"
    ret += "<p>Aceasta platforma isi propune sa valorifice si sa promoveze contributia esentiala a scriitorilor romani la patrimoniul literar national si universal. De-a lungul timpului, literatura romana a cunoscut figuri remarcabile ale gandirii, creativitatii si expresivitatii artistice, ale caror opere au marcat profund constiinta colectiva.</p>"
    ret += "<p>In aceasta sectiune, ne vom opri asupra uneia dintre personalitatile de seama ale literaturii romane: <b>Ioan Slavici<b>. Prozator, jurnalist si om de cultura, Slavici a surprins in scrierile sale viata satului ardelean si complexitatea sufletului taranului roman, contribuind decisiv la conturarea realismului romanesc. Vom explora viata sa, temele centrale ale operei si mostenirea literara pe care a lasat-o generatiilor urmatoare.</p>"
    ret += f"<a href={url_for('scriitor')}>Aflati mai multe detalii despre scriitorul Ioan Slavici</a>"
    return ret

@app.route("/Ioan_Slavici", methods=['GET'])
def scriitor():
    ret = "<center><h1>Ioan Slavici</h1></center>"
    ret += "<h2>O viata dedicata literaturii si realitatii rurale</h2>"
    ret += "<p>Ioan Slavici (1848-1925) a fost unul dintre cei mai importanti scriitori romani din secolul XIX, un nume de referinta in literatura realista. Nascut intr-o familie de tarani din Ardeal, in satul Siria, Slavici a avut o educatie temeinica si a fost profund influentat de conditiile sociale si economice ale vremii. A studiat la Timisoara si la Viena, unde a intrat in contact cu ideile iluministe si nationale care aveau sa-i modeleze viziunea literara.</p>"
    ret += "<p>Opera sa este strans legata de viata si sufletul satului romanesc, iar una dintre marile sale realizari este abilitatea de a reda atat viata cotidiana a taranilor, cat si complexitatea psihologica a acestora. Scrierile sale nu sunt doar o simpla relatare a unor evenimente, ci o analiza profunda a relatiilor umane, a conflictelor interioare si a moravurilor sociale.</p>"
    ret += "<p>In ciuda succesului sau literar, Slavici a trait o viata marcata de tragedii personale si de dificultati economice. A fost si un om politic, sustinand cu tărie drepturile taranilor si modernizarea Romaniei, dar si un jurnalist activ. Cea mai mare parte a operei sale se concentreaza asupra problemelor sociale ale timpului sau, iar „Moara cu noroc” ramane, fara indoiala, varful carierei sale literare.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"<a href={url_for('curent_lit')}>Curent literar</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Ioan_Slavici/Opera_reprezentativa", methods=['GET'])
def opera_rep():
    ret = "<center><h1>" +feature.gaseste_opera_reprezentativa() + "</h1></center>"
    ret += "<p>„Moara cu noroc” (1881) este cel mai cunoscut si apreciat roman al lui Ioan Slavici, un roman emblematic al realismului romanesc. Aceasta lucrare reflecta perfect preocuparile autorului pentru portretizarea detaliata a vietii rurale si a conditiilor sociale ale taranilor din Ardeal, dar si analiza profunda a naturii umane si a conflictelor morale.</p>"
    ret += "<p>Romanul spune povestea lui Ghita, un tanar satean care, impreuna cu sotia sa, Ana, se muta la o moara din apropierea unui rau, in speranta unei vieti mai bune. Aici, Ghita ajunge sa cunoasca o serie de personaje care il influenteaza profund, printre care si Luca, un om periculos care ii devine „prieten” si care il va atrage in lumea pacatului si a coruptiei. Pe masura ce Ghita se lasa prins in capcana banilor si a ambitiilor personale, soarta sa si a familiei sale ia o turnura tragica.</p>"
    ret += "<p>Tema centrala a romanului este conflictul moral, ilustrat prin alegerea personajelor intre bine si rau, dar si lupta interioara a acestora cu propriile dorinte si slabiciuni. „Moara cu noroc” pune in evidenta natura coruptoare a banilor si pericolele dorintei necontrolate de imbogatire. Povestea de viata a lui Ghita si a celor din jurul sau reprezinta o reflectie asupra destinului, dar si o critica sociala a conditiilor de viata din acea perioada.</p>"
    ret += "<p>Prin aceasta opera, Slavici reuseste sa surprinda complexitatea psihologica a personajelor sale si sa ofere o imagine realista si fidela a satului romanesc din Transilvania. „Moara cu noroc” este considerata o capodopera a literaturii romane, fiind un exemplu de studiu al caracterului uman si al influentei mediului asupra individului.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('curent_lit')}>Curent literat</a><br>"
    ret += f"<a href={url_for('scriitor')}>Ioan Slavici</a><br>"
    ret += f"<a href={url_for('acasa')}>Acasa</a>"
    return ret

@app.route("/Ioan_Slavici/Curent_literar", methods=['GET'])
def curent_lit():
    ret = "<center><h1>"+ feature.gaseste_curent_literar() + "</h1></center>"
    ret += "<p>Realismul este un curent literar care a aparut in Europa in a doua jumatate a secolului XIX, ca o reactie impotriva idealizarii si fanteziei romantismului. Spre deosebire de romantici, care accentuau subiectivismul si idealizarea lumii, realistii si-au propus sa reprezinte realitatea asa cum este, fara exagerari sau embellishments. In literatura romana, realismul a inceput sa se impuna in jurul anilor 1860 si a atins apogeul in ultima parte a secolului XIX.</p>"
    ret += "<p>Principalele trasaturi ale realismului sunt:</p>"
    ret += "<p>Obiectivitatea si fidelitatea fata de realitate: Scriitorii realisti isi propuneau sa descrie lumea asa cum este, sa prezinte viata cotidiana si sa analizeze in detaliu comportamentele si conflictele interioare ale personajelor. Acest curent respinge idealizarea personajelor sau a situatiilor, concentrandu-se pe problemele sociale si economice ale vremii.</p>"
    ret += "<p>Personaje complexe si profund dezvoltate: In operele realiste, personajele nu sunt simple tipologii, ci fiinte complexe, cu motivatie si conflicte interne. Scriitorii realisti analizeaza psihologia acestora si le expun trasaturile intr-un mod detaliat, pentru a arata cum se formeaza si evolueaza comportamentele lor in functie de mediul social.</p>"
    ret += "<p>Interesul pentru societate si problemele sale: Realismul este profund ancorat in realitatile sociale. Scriitorii realisti sunt adesea preocupati de nedreptatile sociale, de conditiile de viata ale diferitelor clase sociale, si de lupta indivizilor pentru supravietuire si progres. De asemenea, exista o preocupare pentru efectele educatiei, ale economiei si ale relatiei de putere.</p>"
    ret += "<p>Limbajul si stilul: Realismul pune accent pe un limbaj clar, direct, care reflecta vorbirea cotidiana. Scriitorii evita ornamentele stilistice excesive si se concentreaza pe precizia si autenticitatea exprimarii.</p>"
    ret += "<p>In contextul literaturii romane, Ioan Slavici este unul dintre cei mai reprezentativi autori ai realismului. Opera sa, in special romanul „Moara cu noroc”, este o manifestare clara a principiilor acestui curent literar. In aceasta lucrare, Slavici prezinta viata unui taran simplu, care ajunge sa fie corupt de dorinta de imbogatire. Conflictul sau interior si influentele negative ale mediului inconjurator sunt trasaturi tipice ale realismului, iar critica sociala este un alt element central.</p>"
    ret += "<p>Realismul, prin obiectivitatea sa, nu doar ca reflecta realitatea, dar o si analizeaza critic, iar literatura acestui curent joaca un rol important in intelegerea profunda a societatii si a psihologiei umane din acea perioada.</p>"
    ret += "<h2>Meniu de navigare</h2>"
    ret += f"<a href={url_for('opera_rep')}>Opera reprezentativa</a><br>"
    ret += f"<a href={url_for('scriitor')}>Ioan Slavici</a><br>"
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
