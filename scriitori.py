import sys

from flask import Flask, url_for
from app.libs import biblioteca_scriitori_opera
from app.libs import biblioteca_scriitori_gen

print ('Scriitori')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1> Scriitori</h1>"

    # Adaug butoanele pentru paginile secundare
    ret += "<h3>Aceasta pagina este dedicata scriitorilor din toata lumea. Scriitorul ales de studentul Mihaila Adelin-Gabriel:</h3>"
    ret += f"<a href={url_for('scriitor')}>Tahereh Mafi</a><br>"
    ret += f"<a href={url_for('opera_literara')}>Tahereh Mafi Magnum Opus</a><br>"
    ret += f"<a href={url_for('gen_literar')}>Genul literar abordat de Tahereh Mafi</a><br>"

    return ret

@app.route("/scriitor", methods=['GET'])
def scriitor():
    ret = "<h1>Tahereh Mafi - Scriitor</h1>"
    ret += "<p>Tahereh Mafi (născută pe 10 noiembrie 1988) este o autoare irano-americană stabilită în Santa Monica, California. Este cunoscută pentru romanele sale de ficțiune pentru tineri (young adult).</p>"
    ret += "<p>Mafi s-a născut pe 9 noiembrie 1988, într-un orășel din statul Connecticut. Este cel mai mic copil din familie și are patru frați mai mari. Părinții ei sunt imigranți din Iran. La vârsta de 12 ani s-a mutat împreună cu familia în nordul Californiei, iar la 14 ani s-au stabilit în Orange County. A absolvit University High School din Irvine, California, iar mai târziu a absolvit Soka University of America din Aliso Viejo, California. Vorbește, la diferite niveluri, opt limbi străine. În timpul facultății, a studiat un semestru în Barcelona, Spania, unde a avut ocazia să se imerseze complet în limba spaniolă.</p>"
    ret += "<p>Mafi a declarat că, înainte de a scrie primul său roman, Shatter Me, a redactat cinci manuscrise pentru a înțelege mai bine cum se scrie o carte. Shatter Me a fost publicat pe 15 noiembrie 2011. De atunci, au urmat volumele Unravel Me (publicat pe 5 februarie 2013) și Ignite Me (publicat pe 4 februarie 2014). Seria Shatter Me include și cinci nuvele: Destroy Me, Fracture Me, Shadow Me, Reveal Me și Believe Me. Drepturile de ecranizare pentru Shatter Me au fost achiziționate de 20th Century Fox. În august 2016, Mafi a lansat Furthermore, un roman middle-grade despre o fată palidă care trăiește într-o lume plină de culoare și magie, dar de care ea pare lipsită. În aprilie 2017, Mafi a anunțat o nouă trilogie în universul Shatter Me, continuând povestea cu aceleași personaje. Primul volum, Restore Me, este narat dintr-o perspectivă dublă: Juliette Ferrars, protagonista, și Warner, antagonistul trilogiei originale. Restore Me a fost publicat pe 6 martie 2018. Următoarea carte a lui Mafi, A Very Large Expanse of Sea, a fost lansată pe 16 octombrie 2018. A fost inclusă pe lista lungă pentru Premiul Național pentru Literatură pentru Tineret din 2018. Vrei să îți ofer o listă cronologică a tuturor cărților scrise de Tahereh Mafi?</p>"
    ret += "<p>În prezent, Mafi locuiește în Irvine, California, unde continuă să scrie. În 2013, s-a căsătorit cu autorul Ransom Riggs. În martie 2017, Mafi a anunțat pe Twitter că este însărcinată, iar pe 30 mai 2017 a născut o fetiță, pe nume Layla. Ea se identifică drept musulmană.</p>"
    ret += f"<a href={url_for('index')}>Scriitori</a><br>"
    ret += f"<a href={url_for('opera_literara')}>Tahereh Mafi Magnum Opus</a><br>"
    ret += f"<a href={url_for('gen_literar')}>Genul literar abordat de Tahereh Mafi</a><br>"

    return ret

@app.route("/scriitor/opera", methods=['GET'])
def opera_literara():
    ret = "<h1>Tahereh Mafi - </h1>" + biblioteca_scriitori_opera.magnum_opus()
    ret += "<p>Shatter Me este un thriller romantic distopic pentru adolescenți, scris de Tahereh Mafi și publicat pe 15 noiembrie 2011. Cartea este narată de Juliette, o fată de 17 ani cu o atingere letală, și se remarcă printr-un stil narativ inedit, care include pasaje și fraze tăiate — asemenea însemnărilor dintr-un jurnal intim. Shatter Me este prima dintr-o serie de șapte volume. Următoarele cărți din serie sunt:</p>"
    ret += "<p>Unravel Me – publicată pe 5 februarie 2013</p>"
    ret += "<p>Ignite Me – publicată pe 4 februarie 2014</p>"
    ret += "<p>Restore Me – publicată pe 6 martie 2018</p>"
    ret += "<p>Defy Me – publicată pe 2 aprilie 2019</p>"
    ret += "<p>Imagine Me – publicată pe 31 martie 2020</p>"
    ret += "<p>Believe Me – publicată pe 11 noiembrie 2021</p>"
    ret += "<p>În ceea ce privește inspirația din spatele seriei, Mafi a declarat că s-a bazat pe „interesul pentru natura umană și capacitatea umanității de a depăși obstacole majore”.</p>"
    ret += "<p>Rezumat în limba română al romanului Shatter Me de Tahereh Mafi:</p>"
    ret += "<p>Juliette Ferrars este o adolescentă de 17 ani cu o putere neobișnuită și periculoasă: atingerea ei este letală și poate ucide pe oricine o atinge pentru o perioadă suficient de lungă. Cu 264 de zile înainte de începutul romanului, ea este internată într-un azil după ce, la vârsta de 14 ani, a ucis accidental un băiețel prin simpla atingere.</p>"
    ret += "<p>La începutul cărții, stilul narativ include numeroase fraze tăiate și o scriitură haotică, reflectând tulburarea mentală și instabilitatea emoțională a lui Juliette. Spre surprinderea ei, primește un coleg de celulă: Adam Kent, care îi pare vag cunoscut. Inițial, sunt distanți, dar treptat se apropie pe măsură ce Juliette îi arată cum să se descurce în azil.</p>"
    ret += "<p>Curând, Guvernul Reestablishment – o organizație totalitară care conduce lumea – vine după Juliette. Adam este dezvăluit a fi soldat al lui Warner, comandantul Sectorului 45 și fiul liderului suprem al Reestablishmentului. Warner o scoate pe Juliette din azil cu condiția să folosească puterea ei pentru a tortura prizonieri în scopuri militare. Deși Warner este fascinat de puterea ei și vrea să o simtă, Juliette refuză să-l rănească, așa că este forțată să tortureze un soldat și un copil într-o cameră de simulare.</p>"
    ret += "<p>Între timp, Juliette și Adam dezvoltă o relație romantică. Se dezvăluie că Adam o cunoștea pe Juliette de dinaintea azilului și că o iubește, iar, mai mult, este imun la atingerea ei. Adam o ajută să evadeze, dar în timpul fugii, Warner o atinge și se dovedește că și el poate supraviețui contactului cu ea.</p>"
    ret += "<p>Juliette și Adam se ascund în apartamentul unde locuiește fratele lui Adam, James, în vârstă de 10 ani. Relația lor începe să se tensioneze, deoarece Adam devine posesiv. Kenji Kishimoto, un fost coleg de-al lui Adam, apare și spune că a fost torturat de Warner pentru a-i găsi. Le promite un loc sigur și plănuiesc să fugă împreună. Totuși, Adam și Juliette sunt capturați, iar Warner îl împușcă pe Adam.</p>"
    ret += "<p>Warner o duce pe Juliette într-o clasă abandonată și îi mărturisește că o iubește, dar ea îl păcălește, îl dezarmează și îl împușcă (fără a-l ucide). Îl salvează pe Adam dintr-un abator, unde era ținut prizonier, și reușesc să scape, deși Adam este grav rănit la picior. Se reîntâlnesc cu Kenji și James, iar Kenji le oferă un refugiu.</p>"
    ret += "<p>Kenji dezvăluie că face parte dintr-o organizație rebelă, Omega Point, care luptă împotriva Reestablishmentului. În cele din urmă, Juliette, Adam și James se alătură Rebeliunii.</p>"
    ret += "<p>Personaje din seria Shatter Me de Tahereh Mafi – descriere în limba română:</p>"
    ret += "<p>Juliette Ferrars: O adolescentă de 17 ani care, la începutul seriei, este speriată, traumatizată și lipsită de încredere, după o viață întreagă de abuzuri, izolare și stigmatizare din cauza atingerii ei letale. Are dificultăți în a avea încredere în ceilalți și în a lega prietenii. Cu toate acestea, este o persoană empatică și bună, mai ales față de cei vulnerabili. De-a lungul seriei, învață să-și controleze puterile și devine mai curajoasă și mai sigură pe sine, cu ajutorul antrenamentelor de la Omega Point. Este, totuși, ușor de influențat și manipulabilă, iar încrederea în sine fluctuează.</p>"
    ret += "<p>Aaron Warner: Conducătorul Sectorului 45 din Reestablishment, în vârstă de 19 ani, descris ca fiind de o frumusețe aproape inumană — are ochi verzi, păr blond-auriu și o înălțime de 1,75 m. La început, este prezentat ca un personaj rece, calculat și manipulativ. Pe parcursul seriei, evoluează și devine mai uman și afectuos. Este profund îndrăgostit de Juliette încă de la început, într-o relație care pornește ca o obsesie. Deși el se consideră lipsit de umanitate, Juliette îl vede ca pe un om normal și dezvoltă empatie față de el. Warner este una dintre puținele persoane care o pot atinge pe Juliette fără a suferi consecințe.</p>"
    ret += "<p>Kenji Kishimoto: Soldat de 20 de ani în armata lui Warner și prieten apropiat al lui Adam. Se dovedește a fi membru al Omega Point și are abilitatea de a deveni invizibil. Este carismatic, glumeț și deseori aduce o notă comică în poveste prin ego-ul său exagerat. Dezvoltă o relație de prietenie profundă cu Juliette, apropiindu-se de ea ca un frate.</p>"
    ret += "<p>James Kent: Fratele mai mic al lui Adam, în vârstă de 10 ani. Este extrem de matur pentru vârsta lui, curios și atent la lumea din jur. Îl admiră profund pe Adam și este protector față de el.</p>"
    ret += "<p>Castle: Liderul Rebeliunii (Omega Point), un om de 44 de ani, om de știință, cu abilități telekinetice. Este înțelept, echilibrat și compasiv. Este primul care o acceptă pe Juliette în rândurile Rebeliunii, deși ascunde multe adevăruri despre identitatea ei reală.</p>"
    ret += "<p>Adam Kent: Soldat în armata Reestablishmentului, în vârstă de 18 ani, responsabil cu supravegherea lui Juliette după scoaterea ei din izolare. Este descris ca având ochi albaștri, păr brunet și tatuaje, cu o înălțime de aproximativ 1,80 m. A fost îndrăgostit de Juliette încă din copilărie. O poate atinge fără a fi rănit, dar acest lucru îi consumă multă energie și îi provoacă durere.</p>"
    ret += "<p>Lista seriei:</p>"
    ret += "<p>1.Shatter Me</p>"
    ret += "<p>1.5. Destroy Me</p>"
    ret += "<p>2.Unravel Me</p>"
    ret += "<p>2.5. Fracture Me</p>"
    ret += "<p>3.Ignite Me</p>"
    ret += "<p>4.Restore Me</p>"
    ret += "<p>4.5. Shadow Me</p>"
    ret += "<p>5.Defy Me</p>"
    ret += "<p>5.5. Reveal Me</p>"
    ret += "<p>6.Imagine Me</p>"
    ret += "<p>6.5. Believe Me</p>"
    ret += "<p>Shatter Me este primul roman din serie. O nuvelă e-book, povestită din perspectiva lui Warner, Destroy Me, care se petrece după Shatter Me și înainte de continuare, a fost lansată pe 6 octombrie 2012. Unravel Me, al doilea roman din serie, a fost lansat pe 5 februarie 2013. O a doua nuvelă e-book, intitulată Fracture Me, care se petrece în timpul și imediat după ultimele momente din Unravel Me, povestită din perspectiva lui Adam, a fost lansată pe 17 decembrie 2013. Al treilea roman din serie, intitulat Ignite Me, a fost lansat pe 4 februarie 2014. În aceeași zi, Unite Me, care conține cele două nuvele combinate pentru prima dată în format tipărit, precum și o privire exclusivă în jurnalul lui Juliette, a fost, de asemenea, lansat.</p>"
    ret += "<p>În aprilie 2017, s-a anunțat că Mafi va lansa încă trei cărți în seria Shatter Me, începând cu Restore Me, care a fost publicat pe 6 martie 2018. O nuvelă intitualată Shadow Me, povestită din perspectiva lui Kenji, a fost lansată pe 5 martie 2019. La o lună după, al cincilea volum din serie, Defy Me, a fost lansat. Al șaselea și ultimul volum principal din Shatter Me, intitulat Imagine Me, a fost lansat pe 31 martie 2020.</p>"
    ret += "<p>„Believe Me”, o a cincea nuvelă scrisă din perspectiva lui Warner, a fost lansată pe 16 noiembrie 2021.</p>"
    ret += "<p>Unite Me: O compunere a primelor două nuvele, Destroy Me și Fracture Me.</p>"
    ret += "<p>Find Me: O compunere a celor de-a treia și patra nuvelă, Shadow Me și Reveal Me.</p>"
    ret += "<p>Pe 20 august 2024, Mafi a anunțat un spin-off al seriei intitulat Shatter Me: The New Republic. Prima instalare, Watch Me, urmează să fie lansată pe 15 aprilie 2025. Plasat la zece ani după evenimentele din Believe Me, romanul va urmări căutarea lui James Anderson de a distruge ultimul refugiu al Reestablishmentului pe Insula Ark.</p>"
    ret += f"<a href={url_for('index')}>Scriitori</a><br>"
    ret += f"<a href={url_for('scriitor')}>Tahereh Mafi</a><br>"
    ret += f"<a href={url_for('gen_literar')}>Genul literar abordat de Tahereh Mafi</a><br>"
    return ret

@app.route("/scriitor/gen", methods=['GET'])
def gen_literar():
    ret = "<h1>Genul literar abordat de Tahereh Mafi</h1>" + biblioteca_scriitori_gen.genre()
    ret += "<p>Genul literar romance young adult dystopian combină elemente din mai multe subgenuri literare și atrage o audiență largă, în special adolescenți și tineri adulți. Acest tip de literatură combină tematici romantice cu povești plasate în societăți distopice, creând o atmosferă tensionată și adesea provocatoare.
    ret += "<p>Young Adult (YA)</p>"
    ret += "<p>Young Adult (sau YA) se referă la cărțile destinate adolescenților cu vârste între 12 și 18 ani, dar care sunt adesea citite și de adulți. Cărțile YA abordează experiențele și problemele cu care tinerii se confruntă sau se pot identifica, cum ar fi relațiile, identitatea și creșterea personală. Protagonistul este, de obicei, un tânăr care se confruntă cu provocările vârstei, iar temele comune includ iubirea, prietenia și conflictele interioare.</p>"
    ret += "<p>Dystopian</p>"
    ret += "<p>Genul distopic descrie o lume viitoare sau alternativă, adesea marcată de o societate opresivă, totalitară și de condiții de viață dificile. În acest tip de lume, există de obicei o ierarhie strictă, cu control guvernamental, supraveghere constantă și inegalități extreme. Protagonistul este adesea un tânăr care se luptă pentru a supraviețui sau pentru a schimba această ordine opresivă.</p>"
    ret += "<p>Romance</p>"
    ret += "<p>Elementul romantic este esențial în acest gen. În majoritatea cazurilor, cărțile YA distopice sunt centrate pe relațiile romantice dintre personaje, de multe ori pe iubirea dintre protagonistă și un alt personaj semnificativ. Relațiile romantice pot fi pline de conflicte, iar iubirea poate deveni o sursă de refugiu sau o piedică în fața luptei pentru supraviețuire.</p>"
    ret += "<p>Caracteristici ale unui roman YA distopic romantic</p>"
    ret += "<p>Conflictul între iubire și supraviețuire: Personajele romantice se confruntă cu dileme între dorințele lor personale și necesitatea de a supraviețui într-o lume periculoasă și opresivă. Relațiile lor pot fi o sursă de confort, dar și de pericol.</p>"
    ret += "<p>Lumea distopică: În aceste romane, lumea este de obicei una în care resursele sunt limitate și libertățile individuale sunt restricționate. Guvernul sau o forță externă controlează societatea, iar protagonistul trebuie să se confrunte cu această realitate grea.</p>"
    ret += "<p>Romantismul în contrast cu pericolele: Relațiile romantice în aceste cărți sunt adesea intense din cauza riscurilor la care sunt expuse personajele. Dragostea devine un factor important în dezvoltarea și evoluția personajelor, dar și un factor de risc, într-o lume unde orice pas greșit poate duce la pierderea libertății sau chiar la moarte.</p>"
    ret += f"<a href={url_for('index')}>Scriitori</a><br>"
    ret += f"<a href={url_for('scriitor')}>Tahereh Mafi</a><br>"
    ret += f"<a href={url_for('opera_literara')}>Tahereh Mafi Magnum Opus</a><br>"
    return ret

@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
