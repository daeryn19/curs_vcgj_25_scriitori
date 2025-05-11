# curs_vcgj_25_scriitori

`Scriitori`
=====================================

# Cuprins

1. [Descriere aplicatie] (#descriere-aplicatie)
2. [Descriere versiune](#descriere-versiune)
3. [Configurare](#configurare)
4. [Exemple pagina web](#exemple-pagina-web)
5. [Testare cu pytest](#testare-cu-pytest)
6. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
7. [Containerizare cu Docker] (#containerizare-docker)
8. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
9. [Bibliografie](#bibliografie)

# Descriere aplicatie
[cuprins](#cuprins)

Aplicatia scriitori prezinta informatii despre cititorul ales de studentul Mihaila Adelin-Gabriel, Tahereh Mafi.
Poate fi executata doar pe Linux. A fost testata pe Ubuntu 24.04.02.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, afiseaza informatii despre autor - disponibile la butonul "Tahereh Mafi" si despre doua atribute ale scriitorului ales: cea mai buna opera a sa - disponibile la butonul "Tahereh Mafi Magnum Opus" si genul literar - disponibile la butonul "Genul literar abordat de Tahereh Mafi".

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini.
Fiecare pagina specifica (cea care afiseaza informatii despre scriitor sau atributele sale) contine un link catre pagina principala.

Aplicatia contine suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inclus unit testing cu pytest, pentru functiile din biblioteca aplicatiei, aflate in directorul `app/libs`.

Pipeline-ul pentru Jenkins este definit in fisierul `Jenkinsfile`. Acesta cloneaza codul, creeaza mediul de lucru virtual (venv), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint)

# Descriere versiune
[cuprins](#cuprins)

##v01 - afisare 'raw' fara formatare. Adaugare link-uri intre pagini.

*ruta standard '/' - URL: http://127.0.0.1:5011
*rute in aplicatia WEB pentru:
  *scriitor: '/scriitor' - URL: http://127.0.0.1:5011/scriitor',
  *cea mai buna opera: '/scriitor/opera' - URL: http://127.0.0.1:5011/scriitor/opera'
  *genul literar: '/scriitor/gen' - URL: http://127.0.0.1:5011/scriitor/gen'

# Configurare
[cuprins](#cuprins)

Configurare .venv si instalare pachete

In directorul 'app' rulati comenzile:

1) activeaza_venv: Incearca sa activeze venv-ul. Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap. La urmatoarea rulare, va activa doar venv-ul.

2) ruleaza_aplicatia: De rulat dupa activarea venv-ului. Va porni serverul pe IP: 127.0.0.1 si port 5011. Acces server din browser: http://127.0.0.1:5011

#EXEMPLU activare venv si rulare
```text
adelingabriel@Ubuntu24:~/SCC/curs_vcgj_25_scriitori$ source activeaza_venv
SUCCESS: venv was activated.
(.venv) adelingabriel@Ubuntu24:~/SCC/curs_vcgj_25_scriitori$ source ruleaza_aplicatia
Scriitori
 * Serving Flask app 'scriitori'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5011
Press CTRL+C to quit
 * Restarting with stat
Scriitori
```

# EXEMPLE pagina web
## Pagina principala
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_mihaila_adelin/img/paginaprincipala.png)

## Pagina scriitorului
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_mihaila_adelin/img/paginascriitor.png)

Functiile din biblioteca de functii a aplicatiei:
- directorul libs, fisierele:
  - biblioteca_scriitori_opera.py
  - biblioteca_scriitori_gen.py
au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functiei cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul quickrequirements.txt. Executia testelor se face cu oricare din comenzile de mai jos, apelate din directorul aplicatiei *scriitor*:
```
   pytest
   python -m pytest
   flask --app scriitori test

   Ultima commanda este posibila datorita implementarii comenzii cli test in aplicatia scriitori.
   Aceasta comanda CLI, apeleaza pytest din program/script:
       pytest.main(["."])
   
   Ultima varianta, desi echivalenta cu primele doua, este mai eleganta.
   Primele doua apeleaza pytest ca fiind ceva extern aplicatiei. 
   Aici insa avem optiunea de a se 'autotesta' inclusa in aplicatie.
```

# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume, variabile, variabile neutilizate, etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

# Containerizare cu Docker
[cuprins](#cuprins)

Cu ajutorul Dockerfile, in acelasi director, pentru a crea imaginea de container trebuie rulata comanda:
  sudo docker build -t scriitori:v01 .
Pentru crearea container-ului si executia sa se ruleaza executa comanda:
  sudo docker run --name scriitori -p 8020:5011 scriitori:v01
  
Pentru vizualizarea tuturor imaginilor existente: 
  sudo docker images

  Exemplu:
```
sudo docker images
[sudo] password for adelingabriel: 
REPOSITORY   TAG           IMAGE ID       CREATED             SIZE
scriitori    v4            50105b320e46   About an hour ago   86.1MB
scriitori    v01           ff5c72a24b7e   4 hours ago         86.1MB
sysinfo      v1            414e82ea2f69   3 weeks ago         276MB
sysinfo      v01           95ea03f27092   7 weeks ago         275MB
sysinfo      v02           95ea03f27092   7 weeks ago         275MB
python       3.10-alpine   2a80925da4ce   5 months ago        51.1MB
```
Imaginea python este cea care sta la baza crearii imaginii folosite pentru containerizarea aplicatiei - scriitori:v4.
Imaginea scriitori creeaza venv-ul, instaleaza pachetele necesare, copiaza codul aplicatiei conform Dockerfile.

Pentru vizualizarea tuturor containerelor, atat pornite, cat si oprite:
  sudo docker ps -a

  Exemplu:
```
sudo docker ps -a
CONTAINER ID   IMAGE           COMMAND              CREATED             STATUS                     PORTS                                       NAMES
a89f2b15b51d   scriitori:v4    "./dockerstart.sh"   About an hour ago   Created                                                                scriitori4
822e93584dff   scriitori:v01   "./dockerstart.sh"   4 hours ago         Exited (0) 4 hours ago                                                 scriitori
2c0a63542a6c   sysinfo:v1      "./dockerstart.sh"   3 weeks ago         Exited (0) 3 weeks ago                                                 sysinfo1
fad78b32f79f   sysinfo:v02     "./dockerstart.sh"   7 weeks ago         Exited (255) 5 weeks ago   0.0.0.0:8020->5011/tcp, :::8020->5011/tcp   sysinfo2
b2ba8a4287fd   sysinfo:v01     "./dockerstart.sh"   7 weeks ago         Exited (0) 7 weeks ago                                                 sysinfo
```
Portul pe calculator unde va raspunde serverul din docker este 8020.
Portul in interiorul containerului este 5011.

Rezultatul executiei containerului va fi vizibil in terminalul de unde s-a dat
comanda.
In consola apar mesajele generate de aplicatia din container.

-d - optiune care trebuie adaugata pentru a rula containerul in background
     altfel, consola din care ruleaza containerul este blocata pe timpul
     rularii acestuia
     
NOTA:
--nume <nume>  este de folosit aceasta optiune.
               altfel docker va crea un string aleator si-l va aloca ca nume
               container-ului pornit

Pentru pornirea/oprirea unui container existent:
  sudo docker stop site
  sudo docker start site
  
In cazul in care containerul nu porneste poate fi folosita comanda de mai jos pentru a crea un container cu imaginea cu probleme care in loc entrypoint-ul configurat va folosi shell ca entrypoint.

  sudo docker run -it --rm --entrypoint sh <image:tag>

Pentru stergerea containerelor/imaginilor:
  sudo docker rm  <container (id, nume)r>
  sudo docker rmi <imagine (id, nume:tag ...)>

# Exemplu executie pipeline Jenkins
[cuprins](#cuprins)

Pentru a se putea executa si ultimul pas din pipeline-ul de Jenkins din acest branch - creare container docker, trebuie ca userul care ruleaza Jenkins sa poata da comenzi de docker, fara sudo + parola.

![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_mihaila_adelin/img/jenkins.png)

# Bibliografie:
[cuprins](#cuprins)
[Github Sysinfo](https://github.com/crchende/sysinfo/blob/simplu_main)

