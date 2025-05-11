# curs_vcgj_25_scriitori


## 📑 Cuprins

1. [ Descriere generală](#-descriere-generală)  
2. [ Structura proiectului](#-structura-proiectului)  
3. [ Funcționalități](#-funcționalități)  
4. [ Comenzi utile](#-comenzi-utile)  
5. [ Teste cu unittest](#-teste-unitare)  
6. [ Automatizare Jenkins](#️-automatizare-jenkins)  
7. [ Bibliografie](#-Bibliografie)

---

## Descriere generală

Aplicația Scriitori – John Steinbeck este un proiect dezvoltat în Python, care oferă o prezentare a vieții și operelor scriitorului american John Steinbeck. Aceasta rulează ca o aplicație web minimalistă, construită cu framework-ul Flask, și permite accesarea rapidă a informațiilor printr-o interfață simplă, organizată pe mai multe rute.

Fișierul principal al aplicației gestionează trei rute: pagina principală (/), descrierea autorului (/descriere), o listă cu operele importante (/carti) si curentul literar.

Conținutul afișat este generat din funcții separate, organizate în module proprii, stocate în directorul app/lib/.

Proiectul include și o componentă de testare automată. Folosind framework-ul unittest, au fost scrise teste pentru funcțiile principale ale aplicației, care verifică integritatea datelor afișate și corectitudinea tipurilor returnate.

Pentru analiză statică a codului, aplicația este integrată cu pylint, iar toate verificările sunt automatizate într-un pipeline Jenkins. Acest pipeline rulează toate etapele importante:

1. clonarea codului

2. crearea și activarea unui mediu virtual (venv)

3. instalarea dependențelor din quickrequirements.txt

4. rularea testelor și verificărilor

5. construirea imaginii Docker

Aplicația este containerizată complet prin intermediul unui fișier Dockerfile, care permite rularea într-un mediu izolat, fără configurări manuale. Astfel, proiectul este pregătit pentru livrare și testare în medii controlate, fiind un exemplu complet de integrare a conceptelor de dezvoltare modernă: cod Python, web cu Flask, testare, CI și Docker.

---

## Structura proiectului

```
├── app/
│   ├── popa_adrian_scriitori.py (fișier principal Flask)
│   └── lib/
│       ├── descriere.py 
│       └── carti.py 
	└── curent_literar.py 
├── test/
│   └── testare.py 
├── Dockerfile
├── quickrequirements.txt
├── Jenkinsfile
├── .gitignore
└── README.md
```

---

## Funcționalități

- **Rute**
 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute în aplicația web pentru:
   * autor: `/John_Steinbeck`
   * descriere: `/John_Steinbeck/descriere`
   * cărți: `/John_Steinbeck/carti`
   * curent literar: `/John_Steinbeck/curent_literar`

- **Testare cu unittest**
  - Se folosește `unittest` pentru a testa funcțiile principale (`get_descriere`, `get_carti`, `get_curent_literar`) aflate în `app/lib`.
```bash
PYTHONPATH=app python3 -m unittest discover -s test
```

- **Verificare automată a codului**
  - `pylint` rulează automat în Jenkins și verifică calitatea codului
```bash
pylint app/lib/*.py
``

- **Docker**
Aplicația este containerizată printr-un `Dockerfile`. Imaginea se poate construi și rula astfel:

```bash
docker build -t popa_adrian_scriitori_app .
docker run -p 5000:5000 popa_adrian_scriitori_app
```
# DevOps CI

Se folosește Jenkins pentru automatizarea testării și build-ului aplicației.

---

## Comenzi utile

### Creare de fisiere si clonare repo:
```bash
mkdir proiect_scc
cd proiect_scc
git clone https://github.com/daeryn19/curs_vcgj_25_scriitori.git
cd curs_vcgj_25_scriitori

### Activare mediu virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalare dependențe:
```bash
pip install -r quickrequirements.txt
```

### Rulare aplicație:
```bash
python3 popa_adrian_scriitori.py
```

### Build Docker:
```bash
docker build -t popa_adrian_scriitori_app .
docker run -p 5000:5000 popa_adrian_scriitori_app
```

---

## Teste unitare

Fișierul `test/testare.py` conține două clase de test care validează funcțiile `get_descriere()`, `get_carti()` si get_curent_literar. Testele verifică:
- dacă tipul returnat este string
- dacă textul conține numele autorului
- dacă textul conține curentul literar al autorului 

---

## Automatizare Jenkins

Pipeline-ul este definit în fișierul `Jenkinsfile` și conține următoarele etape:

- clonare repo
- creare și activare mediu virtual
- instalare dependințe
- rulare pylint
- rulare teste
- build Docker

## Exemplu execuție pipeline Jenkins

![Pipeline Jenkins](static/images/Testare_Jenkins.xcf)

---

# Bibliografie

- [Documentație Flask](https://flask.palletsprojects.com/)
- [GitHub Docs](https://docs.github.com/)
- [Jenkins Docs](https://www.jenkins.io/doc/)
- [Docker Docs](https://docs.docker.com/)