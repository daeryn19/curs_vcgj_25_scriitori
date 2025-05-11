# Proiect SCC - Ionela Baston

## Scriitor ales: **Liviu Rebreanu**

# LiviuRebreanu
============================

## Cuprins
1. [Descriere aplicație](#descriere-aplicație)
2. [Versiune și status](#versiune-și-status)
  1. [Probleme cunoscute](#probleme-cunoscute)
3. [Configurare și rulare](#configurare-și-rulare)
4. [Containerizare](#containerizare)
5. [Stadiu dezvoltare branch](#stadiu-dezvoltare-branch)
6. [Bibliografie](#bibliografie)

---

## Descriere aplicație

**LiviuRebreanu** este o aplicație web creată în Python, care folosește framework-ul Flask pentru a oferi informații despre scriitorul Liviu Rebreanu.

Proiectul a fost realizat pentru a învăța concepte de bază de lucru cu rute Flask și containerizare Docker. Structura este simplă și permite afișarea a două atribute esențiale: viața și opera scriitorului.

Fișierul principal este `scriitori_baston.py` iar logica este separată într-un modul auxiliar pentru claritate și modularitate.

---
### Interfața aplicației

## Interfață - Pagina Rebreanu

![Pagina principală Rebreanu](img/Liviu_Rebreanu.png)

![Pagina despre viață](img/Vlata_Liviu_Rebreanu.png)

![Pagina cu opere](img/Opere_Liviu_Rebreanu.png)


---

## Versiune și status
**v1.0 – versiune funcțională finalizată**
- Flask funcțional local
- Docker funcțional
- README complet
- Pull Request realizat

### Probleme cunoscute
- Fără interfață grafică HTML
- Nu este inclus un sistem de testare automată

---

## Configurare și rulare

### 1. Activare mediu virtual și instalare Flask

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

### 2. Rulare aplicație local

```bash
python3 app/scriitori_baston.py
```

Aplicația va fi disponibilă la adresa:
 `http://127.0.0.1:5000/rebreanu`

---

## Containerizare

### Dockerfile utilizat:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python3", "app/scriitori_baston.py"]
```

### Comenzi utile

```bash
sudo docker build -t rebreanu-app .
sudo docker run -p 5000:5000 rebreanu-app
```

Aplicația va fi accesibilă la `http://localhost:5000/rebreanu`

---

## Stadiu dezvoltare branch

### Funcționalitate implementată:
- Afișare rută `/rebreanu` + 2 subruturi `/rebreanu/viata` și `/rebreanu/opera`
- Separare logică în modul biblioteca_scriitori.py
- Containerizare Docker

### Stadiul actual:
 Complet funcțional și testat local

### Integrare:
- Pull Request deschis din `devel_baston_ionela` spre `main`

---

## Bibliografie

- https://flask.palletsprojects.com/
- https://docs.docker.com/


