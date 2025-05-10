# Proiect SCC 2025 – Tudor Arghezi

## 🔹 Informații generale
- Nume student: Andreea Abagiu
- PID: 8
- Tema aleasă: Scriitori – Tudor Arghezi
- Branch principal: `main_abagiu_andreea`
- Branch dezvoltare: `devel_abagiu_andreea`

---

## ✅ Funcționalitate implementată
- Aplicație Flask cu 4 rute:
  - `/` – pagina principală
  - `/biografie` – descriere scriitor
  - `/opere` – listă opere
  - `/citat` – citat reprezentativ
- Funcțiile sunt în `app/lib/helper.py`

---

## ✅ Testare
- Fișiere de test în `app/tests/`
- Rulate cu `pytest`, testele verifică:
  - status 200 pentru fiecare rută
  - prezența unor cuvinte-cheie în răspuns
- Testele trec complet (`4 passed`)

---

## ✅ Calitate cod – pylint
- Verificări automate din Jenkins pe:
  - `t_arghezi.py`
  - `app/lib/helper.py`
  - `app/tests/test_t_arghezi.py`

---

## ✅ Docker
- Aplicația rulează într-un container
- `Dockerfile` prezent și testat
- Imaginea se construiește și rulează cu:
  ```bash
  docker build -t arghezi_app .
  docker run -p 5050:5000 arghezi_app
