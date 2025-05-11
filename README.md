# curs_vcgj_25_scriitori
# 📚 Proiect: Ion Creangă – Prezentare interactivă

Acest proiect este o aplicație web ușoară, dezvoltată cu Flask și containerizată folosind Docker, care oferă o prezentare interactivă a vieții și operei lui Ion Creangă. Include pagini tematice și este integrat într-un proces de livrare continuă (CI/CD) cu Jenkins.
---

## 🔧 Tehnologii folosite

- Python 3.12
- Flask
- Gunicorn
- Docker
- Jenkins (CI/CD)
- Pytest & Pylint (testare și verificare stil)

---

## 📂 Structura proiectului
```
.
├── ion_creanga.py           # Cod principal Flask
├── requirements.txt         # Biblioteci necesare
├── Dockerfile               # Configurare Docker
├── Jenkinsfile              # Pipeline CI pentru Jenkins
├── app/
│   ├── lib/
│   │   └── helper.py        # Funcții separate pentru conținut
│   └── tests/
│       └── test_ion_creanga.py  # Teste unitare
└── README.md                # Documentație proiect
```

