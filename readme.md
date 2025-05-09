`scriitori`
===================================
# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Descriere versiune](#descriere-versiune)
1. [Configurare](#configurare)
1. [Exemple pagina web](#exemple-pagina-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [Docker](#docker)
   1. [Creare container](#creare-container)
   1. [Executie container](#executie-container)
   1. [Vizualizare containere](#vizualizare-containere)
   1. [Oprire / pornire container - cu aplicatia din container](#oprire-pornire-container-cu-aplicatia-din-containere)
   1. [Curatenie - stergere containere / imagini](#curatenie-stergere-containere-cu-aplicatia-din-containere)
   1. [Lista de comenzi docker utile:](#lista-comenzi-docker-utile)
1. [DevOps](#devops-ci)
   1. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
1. [Bibliografie](#bibliografie)

# Descriere aplicatie

Aplicația dezvoltată are ca temă scriitori și este parte din proiectul VCGJ din cadrul cursului Servicii Cloud și Containerizare. 
Aceasta este realizată folosind framework-ul Flask, în Python, și conține funcționalitate specifică scriitorului Ioan Slavici.
Funcționalitatea implementată include afișarea informațiilor despre:
Opera reprezentativă – "Moara cu noroc"
Curentul literar – Realism

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini. Fiecare pagina specifica (cea care afiseaza informatii despre Ioan Slavici, opera reprezentativa si curentul literar) contine un link catre celelalte pagini.

Aplicatia include suport pentru containerizare in fisierul Dockerfile din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul app/libs.

DevOps CI. Pipeline-ul pentru Jenkins este definint in fisierul Jenkinsfile. 

Ambele pipeline-uri cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).
# Descriere versiune
## v0.1 – Funcționalitate de bază implementată

* ruta standard '/' - URL: http://127.0.0.1:5011
 * rute in aplicatia WEB pentru:
   * scriitor: '/ioan_slavici' - URL: 'http://127.0.0.1:5011/ioan_slavici',
   * opera reprezentativa: '/opera_reprezentativa' - 'http://127.0.0.1:5011/ioan_slavici/opera_reprezentativa'
   * curent literar:       '/curent_literar'       - 'http://127.0.0.1:5011/ioan_slavici/curent_literar'

# Configurare
[cuprins](#cuprins)

Configurare .venv si instalare pachete

In directorul 'app' rulati comenzile:
1) activeaza_venv: Incearca sa activeze venv-ul. 
                   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
                   La urmatoarea rulare, va activa doar venv-ul.

2) ruleaza_aplicatia: De rulat doar dupa activarea venv-ului. 
                      Va porni serverul pe IP: 127.0.0.1 si port: 5011.
                      Acces server din browser: http://127.0.0.1:501
# EXEMPLU activare venv si rulare
```text
    dana@dana:scriitori$ source activeaza_venv 
    SUCCESS: venv was activated.

   (.venv) dana@dana:scriitori$ source ruleaza_aplicatia 
    scriitori
    WARNING: rand 6 []
     * Serving Flask app 'scriitori'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5011
    Press CTRL+C to quit
     * Restarting with stat
    scriitori
```
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_grancea_dana/images/Screenshot%20from%202025-05-09%2013-53-23.png)


# Exemple pagina web
[cuprins](#cuprins)
## Pagina principala
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_grancea_dana/images/Screenshot%20from%202025-05-09%2013-52-27.png)

## Pagina Ioan Slavici
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_grancea_dana/images/Screenshot%20from%202025-05-09%2013-52-15.png)

## Pagina Opera reprezentativa 
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_grancea_dana/images/Screenshot%20from%202025-05-09%2013-52-03.png)

## Pagina Curent literar
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_grancea_dana/images/Screenshot%20from%202025-05-09%2013-51-20.png)

# Testare cu pytest
[cuprins](#cuprins)

O parte din functiile din biblioteca de functii a aplicatie:
- directorul libs, fisierul:
  - feature.py
au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul quickrequirements.txt.
Executia testelor se face cu oricare din comenzile de mai jos, apelate din directorul aplicatiei - *scriitori*:
```
   pytest
   python -m pytest
   flask --app scriitori test

   Ultima commanda este posibila datorita implementarii comenzii cli test in aplicatia sysinfo.
   Aceasta comanda CLI, apeleaza pytest din program/script:
       pytest.main(["."])
   
   Ultima varianta, desi echivalenta cu primele doua, este mai eleganta.
   Primele doua apeleaza pytest ca fiind ceva extern aplicatiei. 
   Aici insa avem optiunea de a se 'autotesta' inclusa in aplicatie.
```
# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori
```
   pylint scriitory.py
```



# Docker
[cuprins](#cuprins)

## Creare container

Dupa crearea Dockerfile, in acelasi director cu acest fisier - pentru acest caz
scriitori, trebuie executata comanda:
    sudo docker build -t scriitori:v01 .

Aceasta creeaza o imagine de container care poate fi vizualizata cu comanda:
 
    sudo docker images

    ex:
    REPOSITORY                  TAG             IMAGE ID       CREATED       SIZE
    scriitori                     v01             beadef0060e0   2 hours ago   110MB
    python                      3.8-alpine      0ccdcbe88eaa   5 days ago    47.5MB

    Avem doua imagini:
    - imaginea de baza, python:3.8-alpine, folosita pentru a
      crea imaginea scriitori:v01
    - imaginea scriitori, creata pe baza imaginii python, in care se
      creaza venv-ul, se instaleaza pachetele necesare aplicatiei, se copiaza
      codul aplicatiei - conform Dockerfile
     
## Executie container

Pentru a genera un container din fisierul imagine trebuie executata comanda run:

    sudo docker run --name scriitori -p 8020:5011 scriitori:v01 

    Aceasta va crea containerul si va si porni executia acestuia.

    Portul pe calculator unde va raspunde serverul din docker este  - 8020
    Portul in interiorul containerului este                         - 5011.

    Rezultatul executie containerului va fi vizibil in terminalul de unde s-a dat
    comanda.
    In consola apar mesajele generate de aplicatia din container.

    -d - optiune care trebuie adaugata pentru a rula containerul in background
         altfel, consola din care ruleaza containerul este blocata pe timpul
         rularii acestuia
 
    NOTA:
    --nume <nume>  este de folosit aceasta optiune.
                   altfel docker va crea un string aleator si-l va aloca ca nume
                   container-ului pornit

## Vizualizare containere

    - vizualizare continere care ruleaza


    sudo docker ps

    CONTAINER ID   IMAGE                 COMMAND              CREATED          STATUS           PORTS                                       NAMES
    0e9388ac0d7d   scriitori:v01         "./dockerstart.sh"   2 hours ago      Up 22 minutes    0.0.0.0:8020->5011/tcp, :::8020->5011/tcp   scriitori

    - vizualizarea tuturor containerelor (inclusiv cele oprite)


    sudo docker ps -a

    CONTAINER ID   IMAGE                COMMAND              CREATED          STATUS                     PORTS                   NAMES
    0e9388ac0d7d   scriitori:v01        "./dockerstart.sh"   2 hours ago      Exited (0) 6 seconds ago                           scriitori



## Oprire / pornire container - cu aplicatia din container

    sudo docker stop scriitori
    sudo docker start scriitori
    
## Tratare probleme (Debugging)

In cazul in care containerul nu porneste poate fi folosita comanda de mai jos pentru a
crea un container cu imaginea cu probleme care in loc entrypoint-ul configurat va
folosi shell ca entrypoint.

    sudo docker run -it --rm --entrypoint sh <image:tag>


Inspectare container - conectare la container-ul care ruleaza cu shell
--

    sudo docker exec -it dana_scriitori sh

    - vizualizare procese pe container (pot fi date si alte comenzi LINUX)
    
    ~/app $ ps
    PID   USER     TIME  COMMAND
        1 site      0:02 {flask} /home/scriitori/scriitori.venv/bin/python /home/scriitori/scriitori/.venv/bin/flask run -h 0.0.0.0 -p 5011 --reload
        8 site      0:30 /home/scriitori/scriitori/.venv/bin/python /home/scriitori/scriitori/.venv/bin/flask run -h 0.0.0.0 -p 5011 --reload
       11 site      0:00 sh
       17 site      0:00 ps
   
(inchiderea terminalului pe container se face cu 'exit')

## Curatenie - stergere containere / imagini


    sudo docker rm  <container (id, nume)r>
    sudo docker rmi <imagine (id, nume:tag ...)>

## Lista de comenzi docker utile:

        Creare container:            sudo docker build -t <nume>:<tag>
        Vizualizare imagini:         sudo docker images
        Vizualizare containere:      sudo docker ps / sudo docker ps -a
        Rulare container:            sudo docker run -name <nume> -p <port PC>:<port Container> <imagine> [-d] # -d pentru a rula in background
        Stop container:              sudo docker stop
        Start container:             sudo docker start
        Executie shell:              sudo docker exec -it <nume> sh
        Atasare la container:        sudo docker atach <nume>


# DevOps CI
[cuprins](#cuprins)
- CI = Continuous Integration

## Exemplu executie pipeline Jenkins
Pentru a se putea executa si ultimul pas din pipeline-ul de Jenkins din acest branch - creare container docker, trebuie ca userul care ruleaza Jenkins sa poata da comenzi de docker, fara sudo + parola.
Puteti gasi pasii de configurare pe [docs.docker.com - linux-postinstall](https://docs.docker.com/engine/install/linux-postinstall/)
Daca folositi masina virtuala linux, restartati masina dupa ce faceti configuratia.
         
      dana@dana:scriitori$ jenkins
![image](https://github.com/daeryn19/curs_vcgj_25_scriitori/blob/devel_grancea_dana/images/Screenshot%20from%202025-05-09%2014-24-13.png)

# Bibliografie:
[cuprins](#cuprins)
- [Github Sysinfo](https://github.com/crchende/sysinfo/tree/simplu_main)
