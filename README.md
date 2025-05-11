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
Aceasta este realizată folosind framework-ul Flask, în Python, și conține funcționalitate specifică scriitorului ales, in acest caz Agatha Christie.


Pentru o navigare mai ușoară în browser, pagina principală oferă linkuri către celelalte secțiuni ale aplicației. Fiecare pagină dedicată (precum cele care afișează informații despre scriitori sau opere) este accesibilă direct din meniul principal.

Aplicația este pregătită pentru rulare în containere, având un fișier Dockerfile situat în directorul principal.

Pe partea de testare, sunt incluse teste unitare cu pytest pentru o parte dintre funcțiile din biblioteca aplicației, localizate în directorul app/lib.

Pentru DevOps și integrare continuă, pipeline-ul Jenkins este definit în fișierul Jenkinsfile. 

Ambele pipeline-uri cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).
# Descriere versiune
## v0.1 – Funcționalitate de bază implementată

* ruta standard '/' - URL: http://127.0.0.1:5011
 * rute in aplicatia WEB pentru:
   * scriitor: '/Agatha_Christie' - URL: 'http://127.0.0.1:5011/Agatha_Christie',
   * opera reprezentativa: '/opera_reprezentativa' - 'http://127.0.0.1:5011/Agatha_Christie/opera_reprezentativa'
   * curent literar:       '/curent_literar'       - 'http://127.0.0.1:5011/Agatha_Christie/curent_literar'

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

![image](images/activeaza_venv.JPG)
![image](images/ruleaza_aplicatia.JPG)

#Exemplu pagina principala
![image](images/acasa.JPG)

#Pagina Agatha Christie
![image](images/pagina_scriitor.JPG)

#Pagina Opera Reprezentativa
![image](images/opera_rep.JPG)

#Pagina Curent Literar
![image](images/curent_literar.JPG)



# Testare cu pytest
[cuprins](#cuprins)
O parte dintre funcțiile din biblioteca aplicației, aflate în fișierul feature.py din directorul libs, au asociate teste unitare. Aceste teste verifică funcționarea corectă a funcțiilor prin apelarea lor cu valori de intrare cunoscute și compararea rezultatului obținut cu cel așteptat. Dacă rezultatul coincide cu valoarea așteptată, testul este marcat ca PASS; în caz contrar, este considerat FAIL.

Pentru testare s-a folosit pachetul **pytest** din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul requirements.txt.
Executia testelor se face cu oricare din comenzile de mai jos, apelate din directorul aplicatiei - *scriitori*:
```
   pytest
   python -m pytest
   flask --app scriitori test
   
(.venv) hangiu-ana@hangiu-ana-VirtualBox:~/Desktop/proiect_ana/curs_vcgj_25_scriitori$ pytest
============================================================================ test session starts ============================================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/hangiu-ana/Desktop/proiect_ana/curs_vcgj_25_scriitori
configfile: pytest.ini
collected 2 items                                                                                                                                                           

app/test/test_lib.py::test_opera_reprezentativa PASSED                                                                                                                [ 50%]
app/test/test_lib.py::test_curent_literar PASSED                                                                                                                      [100%]

============================================================================= 2 passed in 0.05s =============================================================================
```


# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori
```
pylint scriitory.py

(.venv) hangiu-ana@hangiu-ana-VirtualBox:~/Desktop/proiect_ana/curs_vcgj_25_scriitori$ pylint scriitori.py
************* Module scriitori
scriitori.py:13:0: C0301: Line too long (143/100) (line-too-long)
scriitori.py:14:0: C0301: Line too long (441/100) (line-too-long)
scriitori.py:15:0: C0301: Line too long (110/100) (line-too-long)
scriitori.py:22:0: C0301: Line too long (327/100) (line-too-long)
scriitori.py:23:0: C0301: Line too long (319/100) (line-too-long)
scriitori.py:24:0: C0301: Line too long (555/100) (line-too-long)
scriitori.py:34:0: C0301: Line too long (335/100) (line-too-long)
scriitori.py:35:0: C0301: Line too long (380/100) (line-too-long)
scriitori.py:36:0: C0301: Line too long (359/100) (line-too-long)
scriitori.py:37:0: C0301: Line too long (271/100) (line-too-long)
scriitori.py:47:0: C0301: Line too long (192/100) (line-too-long)
scriitori.py:48:0: C0301: Line too long (439/100) (line-too-long)
scriitori.py:49:0: C0301: Line too long (426/100) (line-too-long)
scriitori.py:50:0: C0301: Line too long (442/100) (line-too-long)
scriitori.py:51:0: C0301: Line too long (262/100) (line-too-long)
scriitori.py:1:0: C0114: Missing module docstring (missing-module-docstring)
scriitori.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
scriitori.py:63:4: C0415: Import outside toplevel (pytest) (import-outside-toplevel)

-----------------------------------
Your code has been rated at 5.62/10

```



# Docker
[cuprins](#cuprins)

##Creare container

Dupa crearea Dockerfile, in acelasi director cu acest fisier - pentru acest caz
scriitori, trebuie executata comanda:
 sudo docker build -t scriitori:v01 .

Aceasta creeaza o imagine de container care poate fi vizualizata cu comanda:
 
    sudo docker images

    ex:
    REPOSITORY                  TAG             IMAGE ID       CREATED       SIZE
    scriitori                     v01           61ce2221d887   1 hour ago    79.7MB
    python                      3.8-alpine      cd39247b02f9   8 months ago    47.4MB

    Sunt utilizate doua imagini Docker:
    - Imaginea de bază: python:3.8-alpine, care servește drept fundament pentru construirea imaginii aplicației.
    - Imaginea aplicației: scriitori:v01, construită pe baza imaginii Python, în care se creează un mediu virtual (venv),
       se instalează pachetele necesare și se copiază fișierele aplicației.
[cuprins](#cuprins)      codul aplicatiei - conform Dockerfile
##Executie container

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

##Vizualizare containere

    - vizualizare continere care ruleaza


    sudo docker ps

    CONTAINER ID   IMAGE                            COMMAND              CREATED          STATUS          PORTS                                       NAMES
    13852c8ac28f   scriitori:v01                    "./dockerstart.sh"   3 hours ago      Up 22 minutes   0.0.0.0:8020->5011/tcp, :::8020->5011/tcp   scriitori

    - vizualizarea tuturor containerelor (inclusiv cele oprite)


    sudo docker ps -a

    CONTAINER ID   IMAGE                            COMMAND              CREATED          STATUS                     PORTS                                       NAMES
    13852c8ac28f  scriitori:v01                      "./dockerstart.sh"   3 hours ago      Exited (0) 10 seconds ago                                            scriitori



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
Pentru ca ultimul pas din pipeline-ul Jenkins — crearea containerului Docker — să poată fi executat corect în acest branch, este necesar ca utilizatorul sub care rulează Jenkins să aibă permisiunea de a executa comenzi Docker.

![image](images/pipeline_ana.JPG)
# Bibliografie:
[cuprins](#cuprins)
- [Github Sysinfo](https://github.com/crchende/sysinfo/tree/simplu_main)
