# Aplicatie Web Scriitori cu Flask, Docker și Jenkins CI

Acest proiect prezintă o simplă aplicație web dezvoltată cu framework-ul Flask, menită să afișeze informații despre scriitori și operele lor. Proiectul demonstrează, de asemenea, pașii necesari pentru containerizarea aplicației folosind Docker și automatizarea procesului de build și testare cu Jenkins Pipeline (Continuous Integration).

În prezent, aplicația conține informații despre F.M. Dostoievski.
## Setup Local (fără Docker)

Pentru a rula aplicația local, fără a utiliza containerizarea Docker:

1.  **Clonați repository-ul:**
    ```bash
    # Dacă nu ați făcut-o deja
    # git clone <URL_repository>
    # cd <director_proiect>
    ```

2.  **Creați și activați un mediu virtual Python:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # Pe Linux/macOS
    # sau .\venv\Scripts\activate # Pe Windows/PowerShell
    ```

3.  **Instalați dependențele:**
    ```bash
    pip install -r quickrequirements.txt
    ```

4.  **Rulați aplicația Flask:**
    * **Metoda 1: Folosind `flask run` (recomandat pentru dezvoltare)**
        Asigurați-vă că sunteți în directorul rădăcină al proiectului și setați variabila de mediu `FLASK_APP`:
        ```bash
        export FLASK_APP=app.445D_scriitori # Setați calea către aplicația Flask ca modul
        flask run # Va rula pe portul 5000 implicit (sau cel configurat în cod)
        ```
    * **Metoda 2: Rulând fișierul direct (folosind block-ul `if __name__ == '__main__':`)**
        Asigurați-vă că sunteți în directorul rădăcină al proiectului:
        ```bash
        python app/445D_scriitori.py # Va rula pe portul 5011 conform codului dvs
        ```

## Rulare Teste

Pentru a rula testele Pytest local (asigurându-vă că au trecut înainte de a construi imaginea Docker sau de a comite codul):

1.  Asigurați-vă că mediul virtual Python este activ și dependențele sunt instalate (vezi "Setup Local").
2.  Rulați testele Pytest din directorul rădăcină al proiectului:
    ```bash
    # Asigurati-va ca PYTHONPATH este setat corect pentru ca testele sa gaseasca modulul 'app'
    PYTHONPATH=$PWD pytest
    ```

## Construire și Rulare Docker

Pentru a construi imaginea Docker și a rula aplicația într-un container:

1.  Asigurați-vă că aveți Docker instalat și pornit pe sistem.
2.  Navigați în terminal în directorul rădăcină al proiectului (unde se află `Dockerfile`).
3.  **Construiți imaginea Docker:**
    ```bash
    sudo docker build -t scriitori:v01 .
    ```
    *(Tag-ul `:v01` este un exemplu; puteți folosi alte versiuni sau omite tag-ul pentru `latest`)*
4.  **Rulați un container din imagine:**
    Această comandă va rula containerul, mapând portul `8020` de pe mașina host la portul `5011` expus de container (conform Dockerfile și codului aplicației).
    ```bash
    sudo docker run --name scriitori_container -p 8020:5011 scriitori:v01

    # Pentru a rula containerul în fundal (detasat), adăugați flag-ul -d:
    # sudo docker run -d --name scriitori_container -p 8020:5011 scriitori:v01
    ```
5.  **Gestionare container (opțional):**
    ```bash
    # Opriți containerul:
    # sudo docker stop scriitori_container

    # Ștergeți containerul (dacă nu l-ați rulat cu --rm):
    # sudo docker rm scriitori_container
    ```

## CI/CD cu Jenkins

Proiectul include un fișier `Jenkinsfile` care definește un pipeline de Continuous Integration în sintaxă Declarative. Acest pipeline este proiectat să ruleze automat pe un server Jenkins configurat și parcurge următoarele etape:

1.  **Install Dependencies in Venv:** Creează un mediu virtual Python izolat în spațiul de lucru al agentului Jenkins și instalează dependențele listate în `quickrequirements.txt` în acest mediu.
2.  **Run Tests in Venv:** Activează mediul virtual creat în etapa anterioară și execută testele Pytest definite în directorul `tests/`. Această etapă validează funcționalitatea codului.
3.  **Build Docker image:** Dacă testele trec cu succes, această etapă construiește imaginea Docker a aplicației folosind `Dockerfile` din rădăcina repository-ului.

Acest pipeline asigură că fiecare modificare adusă codului este testată automat și că o imagine Docker actualizată este construită doar dacă testele trec.

## Utilizare Aplicație Web

După ce aplicația este pornită (fie local, fie într-un container Docker), o puteți accesa într-un browser web:

* **Acces Local (rulată direct cu `python app/445D_scriitori.py`):** `http://127.0.0.1:5011/scriitori`
* **Acces Local (rulată cu `flask run`):** `http://127.0.0.1:5000/scriitori` (sau portul specificat)
* **Acces prin Docker:** `http://127.0.0.1:8020/scriitori` (dacă ați folosit maparea de port `8020:5011` în comanda `docker run`)

Navigați la calea `/scriitori` pentru a vedea pagina principală a aplicației și link-urile către informațiile despre scriitor.

## Cerințe

Pentru a construi și rula acest proiect, aveți nevoie de:

* **Python 3.8+** și `pip` (pentru rulare locală și etapele de instalare/test din Jenkins)
* **Docker Engine** (pentru construirea și rularea imaginilor Docker)
* (Opțional) Un server **Jenkins** cu un agent configurat care are acces la un runtime Python (cu venv și pip) și la un daemon Docker.
