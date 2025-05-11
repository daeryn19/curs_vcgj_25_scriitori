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

Aplicația realizată are ca temă principală scriitorii și face parte din proiectul VCGJ, desfășurat în cadrul cursului „Servicii Cloud și Containerizare”.
Aceasta este realizată folosind framework-ul Flask, în Python, și conține funcționalități specifice scriitoareilui Ruta Sepetys.
Funcționalitatea implementată include afișarea informațiilor despre:
Opera "Sârșitul șoaptelor"
Curentul literar – Ficțiune istorică

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini. Fiecare pagina specifica contine un link către celelalte pagini.

Aplicația oferă suport pentru containerizare prin intermediul fișierului Dockerfile aflat în directorul principal al proiectului.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul app/libs.

DevOps CI. Pipeline-ul pentru Jenkins este definint in fisierul Jenkinsfile. 

Ambele pipeline-uri cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).
# Descriere versiune
## v0.1 – Funcționalitate de bază implementată

* ruta standard '/' - URL: http://127.0.0.1:5011
 * rute in aplicatia WEB pentru:
   * scriitor: '/Ruta_Sepetys' - URL: 'http://127.0.0.1:5011/Ruta_Sepetys',
   * opera reprezentativa: '/opera_reprezentativa' - 'http://127.0.0.1:5011/Ruta_Sepetys/opera_reprezentativa'
   * curent literar:       '/curent_literar'       - 'http://127.0.0.1:5011/Ruta_Sepetys/curent_literar'

# Configurare
[cuprins](#cuprins)

Configurare .venv si instalare pachete

In directorul 'app' rulati comenzile:
1) activeaza_venv: Incearca sa activeze venv-ul. 
                   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
                   La urmatoarea rulare, va activa doar venv-ul.

2) ruleaza_aplicatia: De rulat doar dupa activarea venv-ului. 
                      Va porni serverul pe IP: 127.0.0.1 si port: 5011.
                      Acces server din browser: http://127.0.0.1:5011
# EXEMPLU activare venv si rulare
```text
    hangiu-ana@hangiu-ana:scriitori$ source activeaza_venv 
    SUCCESS: venv was activated.

   (.venv) hangiu-ana@hangiu-ana:scriitori$ source ruleaza_aplicatia 
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

# Exemplu Pagina Principala
![image](images/pag_principala.JPG)

#Exemplu Pagina Ruta Sepetys
![image](images/pag_scriitor.JPG)

# Exemplu Pagina Opera Reprezentativa
![image](images/op_rep.JPG)

#Exemplu Pagina Curent Literar 
![image](images/curent_l.JPG)



# Testare cu pytest
[cuprins](#cuprins)

O parte dintre funcțiile din biblioteca aplicației, aflată în directorul libs (fișierul feature.py), au teste de tip unit-test asociate. Aceste teste presupun apelarea funcției respective și compararea valorii returnate cu valoarea așteptată. Testul va returna PASS dacă valoarea obținută este corectă și FAIL în caz contrar.

Pentru testare, s-a utilizat pachetul pytest din Python, care este inclus în lista de pachete necesare în fișierul requirements.txt. Executarea testelor poate fi realizată folosind oricare dintre comenzile de mai jos, apelate din directorul aplicației scriitori:
```
   pytest
   python -m pytest
   flask --app scriitori test

   Ultima comandă devine posibilă datorită implementării comenzii CLI test în aplicația sysinfo. Această comandă CLI execută    pytest din programul/script utilizând:
       pytest.main(["."])
   
   Deși echivalentă cu primele două opțiuni, această variantă este considerată mai elegantă. În primele două cazuri, pytest    este tratat ca un tool extern aplicației, în timp ce în acest caz opțiunea de autotestare este integrată direct în    aplicație.

   (.venv) hangiu-ana@hangiu-ana-VirtualBox:~/Desktop/proiect_giulia/curs_vcgj_25_scriitori$ pytest
============================================================================ test session starts =============================================================================
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/hangiu-ana/Desktop/proiect_giulia/curs_vcgj_25_scriitori
configfile: pytest.ini
collected 2 items                                                                                                                                                            

app/test/test_lib.py::test_opera_reprezentativa PASSED                                                                                                                 [ 50%]
app/test/test_lib.py::test_curent_literar PASSED                                                                                                                       [100%]

============================================================================= 2 passed in 0.06s ==============================================================================


```
# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori
```
   pylint scriitory.py
   (.venv) hangiu-ana@hangiu-ana-VirtualBox:~/Desktop/proiect_giulia/curs_vcgj_25_scriitori$ pylint scriitori.py
************* Module scriitori
scriitori.py:13:0: C0301: Line too long (223/100) (line-too-long)
scriitori.py:14:0: C0301: Line too long (331/100) (line-too-long)
scriitori.py:15:0: C0301: Line too long (103/100) (line-too-long)
scriitori.py:22:0: C0301: Line too long (170/100) (line-too-long)
scriitori.py:23:0: C0301: Line too long (129/100) (line-too-long)
scriitori.py:24:0: C0301: Line too long (434/100) (line-too-long)
scriitori.py:34:0: C0301: Line too long (183/100) (line-too-long)
scriitori.py:35:0: C0301: Line too long (240/100) (line-too-long)
scriitori.py:36:0: C0301: Line too long (405/100) (line-too-long)
scriitori.py:37:0: C0301: Line too long (124/100) (line-too-long)
scriitori.py:47:0: C0301: Line too long (146/100) (line-too-long)
scriitori.py:49:0: C0301: Line too long (196/100) (line-too-long)
scriitori.py:50:0: C0301: Line too long (266/100) (line-too-long)
scriitori.py:51:0: C0301: Line too long (300/100) (line-too-long)
scriitori.py:52:0: C0301: Line too long (185/100) (line-too-long)
scriitori.py:53:0: C0301: Line too long (276/100) (line-too-long)
scriitori.py:54:0: C0301: Line too long (328/100) (line-too-long)
scriitori.py:1:0: C0114: Missing module docstring (missing-module-docstring)
scriitori.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:66:4: C0415: Import outside toplevel (pytest) (import-outside-toplevel)

------------------------------------------------------------------
Your code has been rated at 5.49/10 (previous run: 5.62/10, -0.13)




```



# Docker
[cuprins](#cuprins)

##Creare container

Dupa crearea Dockerfile, in acelasi director cu acest fisier - pentru acest caz
scriitori, trebuie executata comanda:
 sudo docker build -t scriitori:v02 .

Aceasta creeaza o imagine de container care poate fi vizualizata cu comanda:
 
    (.venv) hangiu-ana@hangiu-ana-VirtualBox:~/Desktop/proiect_giulia/curs_vcgj_25_scriitori$ docker images
REPOSITORY   TAG           IMAGE ID       CREATED             SIZE
scriitori    v02           64ae0e13b54e   5 seconds ago       79.7MB
python       3.8-alpine    cd39247b02f9   8 months ago        47.4MB

    Avem doua imagini:
    - imaginea de baza, python:3.8-alpine, folosita pentru a
      crea imaginea scriitori:v01
    - imaginea scriitori, creata pe baza imaginii python, in care se
      creaza venv-ul, se instaleaza pachetele necesare aplicatiei, se copiaza
[cuprins](#cuprins)      codul aplicatiei - conform Dockerfile
##Executie container

Pentru a genera un container din fisierul imagine trebuie executata comanda run:

    sudo docker run --name scriitori02 -p 8020:5011 scriitori:v02 

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

##Vizualizare containere

    - vizualizare continere care ruleaza


    sudo docker ps

    CONTAINER ID   IMAGE                            COMMAND              CREATED          STATUS          PORTS                                       NAMES
    0e9388ac0d7d   scriitori:v02                  "./dockerstart.sh"    50 minutes ago      Up 22 minutes   0.0.0.0:8020->5011/tcp, :::8020->5011/tcp   scriitori

    - vizualizarea tuturor containerelor (inclusiv cele oprite)

(.venv) hangiu-ana@hangiu-ana-VirtualBox:~/Desktop/proiect_giulia/curs_vcgj_25_scriitori$ sudo docker ps -a
CONTAINER ID   IMAGE           COMMAND              CREATED             STATUS                         PORTS                                       NAMES
e2d99b6b747b   scriitori:v02   "./dockerstart.sh"   53 seconds ago      Exited (0) 11 seconds ago                                                  scriitori02
2a6dbcb7b457   c32c582780ca    "./dockerstart.sh"   4 minutes ago       Created                        0.0.0.0:8020->5011/tcp, :::8020->5011/tcp   scriitori2
8f248ce140d5   dc91b8585c20    "./dockerstart.sh"   About an hour ago   Exited (0) About an hour ago                                               scriitori
a7fac9aedb2b   sysinfo:v01     "./dockerstart.sh"   7 weeks ago         Exited (0) 7 weeks ago                                                     sysinfo

##Oprire / pornire container - cu aplicatia din container

    sudo docker stop scriitori
    sudo docker start scriitori

##Curatenie - stergere containere / imagini


    sudo docker rm  <container (id, nume)r>
    sudo docker rmi <imagine (id, nume:tag ...)>

##Lista de comenzi docker utile:

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
Pentru a putea executa ultimul pas din pipeline-ul Jenkins (crearea containerului Docker) din acest branch, utilizatorul care rulează Jenkins trebuie să aibă permisiunea de a rula comenzi Docker fără a utiliza sudo sau a introduce parola.

Pașii de configurare pot fi găsiți pe docs.docker.com - linux-postinstall.

Dacă utilizați o mașină virtuală Linux, asigurați-vă că reporniți mașina după ce finalizați configurarea.
![image](images/pipeline_giulia.JPG)


# Bibliografie:
[cuprins](#cuprins)
- [Github Sysinfo](https://github.com/crchende/sysinfo/tree/simplu_main)
