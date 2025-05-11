# curs_vcgj_25_scriitori

# 📘 Proiect Scriitori – John Steinbeck  
**Student**: Popa Adrian  
**Grupa**: 443D  
**Profesor**: Conf. Dr. Vlad D.  
**Materie**: Sisteme de Calcul și Comunicații (SCC)  
**An**: 2025  

---

## ✅ Descriere generală

Aplicația Scriitori – John Steinbeck este un proiect educațional dezvoltat în Python, care oferă o prezentare structurată a vieții și operelor scriitorului american John Steinbeck. Aceasta rulează ca o aplicație web minimalistă, construită cu framework-ul Flask, și permite accesarea rapidă a informațiilor printr-o interfață simplă, organizată pe mai multe rute.

Fișierul principal al aplicației gestionează trei rute: pagina principală (/), descrierea autorului (/descriere) si o listă cu operele importante (/carti)

Conținutul afișat este generat din funcții separate, organizate în module proprii, stocate în directorul app/lib/. Această abordare permite întreținerea ușoară și extinderea aplicației.

Proiectul include și o componentă de testare automată. Folosind framework-ul unittest, au fost scrise teste pentru funcțiile principale ale aplicației, care verifică integritatea datelor afișate și corectitudinea tipurilor returnate.

Pentru analiză statică a codului, aplicația este integrată cu pylint, iar toate verificările sunt automatizate într-un pipeline Jenkins. Acest pipeline rulează toate etapele importante:

1. clonarea codului

2. crearea și activarea unui mediu virtual (venv)

3. instalarea dependențelor din quickrequirements.txt

4. rularea testelor și verificărilor

5. construirea imaginii Docker

Aplicația este containerizată complet prin intermediul unui fișier Dockerfile, care permite rularea într-un mediu izolat, fără configurări manuale. Astfel, proiectul este pregătit pentru livrare și testare în medii controlate, fiind un exemplu complet de integrare a conceptelor de dezvoltare modernă: cod Python, web cu Flask, testare, CI și Docker.

---

## 📂 Structura proiectului

```
├── app/
│   ├── John_Steinbeck.py (fișier principal Flask)
│   └── lib/
│       ├── descriere.py (descriere autor)
│       └── carti.py (lista cărți)
├── test/
│   └── test_testare.py (teste unitar)
├── Dockerfile
├── quickrequirements.txt
├── Jenkinsfile
├── .gitignore
└── README_popa_adrian.md
```

---

## 🚀 Funcționalități

- **Rute Flask:**
  - `/` – Pagina de start
  - `/descriere` – Descrierea scriitorului John Steinbeck
  - `/carti` – Listă cu operele importante ale autorului

- **Testare unitară**
  - Folosește `unittest` pentru a verifica funcțiile din `descriere.py` și `carti.py`

- **Verificare automată a codului**
  - `pylint` rulează automat în Jenkins și verifică calitatea codului

- **Docker**
  - Aplicația este containerizată și poate fi rulată izolată pe orice mașină cu Docker

---

## 🔧 Comenzi utile

### 🧪 Activare mediu virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 📦 Instalare dependențe:
```bash
pip install -r quickrequirements.txt
```

### ▶️ Rulare aplicație:
```bash
python3 app/popa_adrian_scriitori.py
```

### 🧪 Rulare teste:
```bash
PYTHONPATH=app python3 -m unittest discover -s test
```

### 🐳 Build Docker:
```bash
docker build -t popa_adrian_scriitori:v1 .
docker run -p 5000:5000 popa_adrian_scriitori:v1
```

---

## 🧪 Teste unitare

Fișierul `test/testare.py` conține două clase de test care validează funcțiile `get_descriere()` și `get_carti()`. Testele verifică:
- dacă tipul returnat este string
- dacă textul conține numele autorului

---

## ⚙️ Automatizare Jenkins

Pipeline-ul este definit în fișierul `Jenkinsfile` și conține următoarele etape:
- Creare și activare `venv`
- Instalare dependențe
- Linting cu `pylint`
- Rulare teste unitare
- Build imagine Docker
- Creare container

---

## 📸 Capturi de ecran 

- Rulare aplicație în browser (`localhost:5000`)
- Build și execuție container Docker
- Jenkins pipeline cu build reușit
- Teste rulate cu succes

---

## ✅ Concluzie

Acest proiect demonstrează integrarea unor concepte cheie de dezvoltare software: modularizare, testare, automatizare și containerizare. Prin utilizarea unor unelte moderne precum **Jenkins** și **Docker**, aplicația poate fi testată și livrată rapid într-un mediu controlat.