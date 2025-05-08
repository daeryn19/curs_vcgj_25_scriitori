# curs_vcgj_25_scriitori

`scriitori`
===================================

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Descriere versiune](#descriere-versiune)
1. [Configurare](#configurare)
1. [Exemple pagina web](#exemple-pagina-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [Utilizare Docker si containerizare alicatie](https://github.com/crchende/sysinfo/blob/main/doc/dockerdoc.md)
1. [DevOps](#devops-ci)
   1. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
1. [Bibliografie](#bibliografie)

# Descriere aplicatie

Aplicația scriitori este o aplicație web educațională care oferă informații despre viața și opera scriitorului Ion Luca Caragiale. Scopul aplicației este de a facilita accesul la date esențiale despre autor și creațiile sale literare într-un mod structurat și accesibil din browser. Partea web a aplicației este construită folosind framework-ul Flask. Codul aplicației este scris în Python și folosește structuri simple pentru a încărca și afișa conținutul informativ, organizat în pagini tematice (operă reprezentativa, curente literare etc.).

Navigarea este intuitivă: pagina principală include link-uri către celelalte secțiuni ale aplicației, iar fiecare pagină tematică include un link de întoarcere la pagina principala.

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul `app/libs`.

`DevOps CI`.
Pipeline-ul pentru Jenkins este definint in fisierul `Jenkinsfile`.

Pipeline-uri cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).

# Descriere versiune
## v0.1 – afisare informatii de baza despre Ion Luca Caragiale. Structura initiala a aplicatiei cu pagina principala si link-uri catre pagini tematice.

 * ruta standard '/' - URL: http://127.0.0.1:5011
 * rute in aplicatia WEB pentru:
   * scriitor: '/Ion_Luca_Caragiale' - URL: 'http://127.0.0.1:5011/Ion_Luca_Caragiale',
   * opera reprezentativa:      '/Opera_reprezentativa'      - URL: 'http://127.0.0.1:5011/Opera_reprezentativa'
   * curent literar: '/Curent_literar' - URL: 'http://127.0.0.1:5011/Curent_literar'


# Configurare
[cuprins](#cuprins)

Clonare repository

Creati spatiul de lucru si clonati aplicatia sysinfo: 

```text   
   mkdir proiect_scc
   cd proiect_scc
   git clone https://github.com/daeryn19/curs_vcgj_25_scriitori.git (aduc repository-ul scriitori de pe git in calculatorul local)

   
```

Configurare .venv

In directorul 'curs_vcgj_25_scriitori' rulati comenzile:

1) activeaza_venv: Incearca sa activeze venv-ul. 
                   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
                   La urmatoarea rulare, va activa doar venv-ul.
                
2) ruleaza_aplicatia: De rulat doar dupa activarea venv-ului. 
                      Va porni serverul pe IP: 127.0.0.1 si port: 5011.
                      Acces server din browser: http://127.0.0.1:5011

# EXEMPLU activare venv si rulare
```text
    (.venv) mara@ubuntu:~/Desktop/proiect_scc/curs_vcgj_25_scriitori$ source activeaza_venv
SUCCESS: venv was activated.
(.venv) mara@ubuntu:~/Desktop/proiect_scc/curs_vcgj_25_scriitori$ source ruleaza_aplicatia
scriitori
 * Serving Flask app 'scriitori'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5011
Press CTRL+C to quit
 * Restarting with stat
scriitori

```

![Captura terminal](static/images/activeaza_aplicatia.png)


# EXEMPLE pagina web 
## Pagina principala

![Captura terminal](static/images/pagina_principala.png)


# Testare cu pytest
[cuprins](#cuprins)

O parte din functiile din biblioteca de functii a aplicatie:
- directorul libs, fisierele:
  - test_biblioteca.py
au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul quickrequirements.txt.

```text

(.venv) mara@ubuntu:~/Desktop/proiect_scc/curs_vcgj_25_scriitori$ pytest
================================================================================= test session starts ==================================================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/mara/Desktop/proiect_scc/curs_vcgj_25_scriitori
configfile: pytest.ini
collected 2 items                                                                                                                                                                      

app/tests/test_biblioteca.py::test_opera_reprezentativa_Caragiale PASSED                                                                                                         [ 50%]
app/tests/test_biblioteca.py::test_curent_literar_Caragiale PASSED                                                                                                               [100%]

================================================================================== 2 passed in 0.02s ===================================================================================
```


# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

```text

(.venv) mara@ubuntu:~/Desktop/proiect_scc/curs_vcgj_25_scriitori$ pylint scriitori.py
************* Module scriitori
scriitori.py:17:0: C0301: Line too long (287/100) (line-too-long)
scriitori.py:18:0: C0301: Line too long (121/100) (line-too-long)
scriitori.py:25:0: C0301: Line too long (166/100) (line-too-long)
scriitori.py:34:0: C0301: Line too long (177/100) (line-too-long)
scriitori.py:44:0: C0301: Line too long (168/100) (line-too-long)
scriitori.py:1:0: C0114: Missing module docstring (missing-module-docstring)
scriitori.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:59:4: C0415: Import outside toplevel (pytest) (import-outside-toplevel)

------------------------------------------------------------------
Your code has been rated at 6.86/10 (previous run: 8.00/10, -1.14)
```

# Docker
[cuprins](#cuprins)

##Creare container

Crearea imaginii scriitori:v01 cu comanda:

sudo docker build -t scriitori:v01 .


Vizualizare imagine cu comanda:

sudo docker ps -a

```text 
    (.venv) mara@ubuntu:~/Desktop/proiect_scc/curs_vcgj_25_scriitori$ sudo docker images
[sudo] password for mara: 
REPOSITORY   TAG           IMAGE ID       CREATED        SIZE
scriitori    v01           1b9b74e75305   2 days ago     86MB
sysinfo      v01           00871cd7feea   7 weeks ago    275MB
```

##Executie container

Generare container cu comanda:

    sudo docker run --name scriitori -p 8020:5011 scriitori:v01 

##Vizualizare containere

```text
(.venv) mara@ubuntu:~/Desktop/proiect_scc/curs_vcgj_25_scriitori$ sudo docker ps -a
CONTAINER ID   IMAGE           COMMAND              CREATED       STATUS                   PORTS     NAMES
172574cc13fb   scriitori:v01   "./dockerstart.sh"   2 days ago    Exited (0) 4 hours ago             scriitori
2a50035b5ada   sysinfo:v01     "./dockerstart.sh"   7 weeks ago   Exited (0) 7 weeks ago             sysinfo
```


# DevOps CI
[cuprins](#cuprins)
- CI = Continuous Integration

## Exemplu executie pipeline Jenkins
![Captura terminal](static/images/jenkins.png)




# Bibliografie:
[cuprins](#cuprins)
- [Github Actions](https://docs.github.com/en/actions)
