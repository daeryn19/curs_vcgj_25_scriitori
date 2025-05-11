# Proiect SCC 2025 – Dmitry Glukhovsky

## 🔹 Informații generale
- Nume student: Paun FLORIN 
- Tema aleasă: Scriitori – Dmitry Glukhovsky  
- Branch principal: main_paun_florin
- Branch dezvoltare: devel_paun_florin

---

## ✅ Funcționalitate implementată
- Aplicație Flask cu 4 rute:
  - `/` – pagina principală  
  - `/despre scriitor` – descriere scriitor  
  - `/opere` – listă opere (ex: Metro 2033, Metro 2034, Metro 2035)  

---

## ✅ Testare
- Fișiere de test în `app/tests/`  
- Rulate cu `pytest`, testele verifică:
  - status 200 pentru fiecare rută  
  - prezența unor cuvinte-cheie relevante (ex: „Metro”, „subteran”, „post-apocaliptic”) în răspunsuri  
- Testele trec complet (`2 passed`)  

---

## ✅ Calitate cod – pylint
- Verificări automate din Jenkins pe:
  - `t_glukhovsky.py`  
  - `app/lib/helper.py`  
  - `app/tests/test_d_glukhovsky.py`  

---

## ✅ Docker
- Aplicația rulează într-un container  
- `Dockerfile` prezent și testat  
- Imaginea se construiește și rulează cu:  
  sudo docker build -t scriitori_dmitry_glukhovsky .  
  sudo docker run -p 5011:5011 scriitori_dmitry_glukhovsky
