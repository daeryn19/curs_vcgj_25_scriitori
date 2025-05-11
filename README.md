# curs_vcgj_25_scriitori

Aplicație educațională despre scriitori străini – Victor Hugo.

---

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)  
2. [Versiune](#versiune)  
3. [Configurare](#configurare)
4. [Functionalitati](#functionalitati)
5. [Exemple pagină web](#exemple-pagină-web)  
6. [Testare cu pytest](#testare-cu-pytest)  
7. [Utilizare Docker și containerizare aplicație](#docker)  
8. [DevOps CI - Jenkins](#devops-ci)  
9. [Bibliografie](#bibliografie)  

---

## Descriere aplicație

Aplicația **Scriitori** este o aplicație web simplă, realizată cu Flask, care oferă informații despre viața și opera scriitorului **Victor Hugo**.

- Pagina principală afișează un meniu cu scriitorul.
- Fiecare scriitor are pagini dedicate pentru:
  - opere reprezentative
  - descriere scriitor

Aplicația este testată cu `pytest`, containerizată cu Docker și automatizată cu Jenkins CI.

---

## Versiune

**v0.1** – Funcționalitate minimă:  
- pagini pentru scriitor, operă și curent literar  
- testare automată  
- fișiere pentru CI și containerizare  

---

## Configurare

### Clonare repository

```bash
git clone -b devel_nume_tău https://github.com/nume-user/curs_vcgj_25_scriitori.git
cd curs_vcgj_25_scriitori

### Configurare mediu virtual

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Rulare aplicație

```bash
export FLASK_APP=app/443D_scriitori.py
flask run
```


Accesează în browser:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)



