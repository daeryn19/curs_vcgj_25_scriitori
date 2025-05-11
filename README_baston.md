# Proiect SCC - Ionela Baston

## Scriitor ales: **Liviu Rebreanu**

### Ce am făcut:

- Am creat o aplicație Flask cu rute:
  - `/rebreanu`
  - `/rebreanu/viata`  - `/rebreanu/opera`
- Am scris funcții separate în `biblioteca_scriitori.py` pentru a returna informații despre viață și opere.
- Am testat aplicația local cu succes.
- Am creat un Dockerfile și am construit containerul cu:
  - `sudo docker build -t rebreanu-app .`
  - `sudo docker run -p 5000:5000 rebreanu-app`
- Aplicația rulează în browser pe: `http://localhost:5000/rebreanu`

