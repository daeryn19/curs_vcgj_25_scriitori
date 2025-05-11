# curs_vcgj_25_scriitori

# 📚 Proiect: Nichita Stănescu – Prezentare interactivă

Acest proiect este o aplicație web simplă, construită în Flask și containerizată cu Docker, care prezintă informații despre viața și opera poetului **Nichita Stănescu**. Este inspirat de un proiect similar cu animale, adaptat pentru un scriitor român.

---

## 🔧 Tehnologii folosite

- Python 3.10
- Flask
- Gunicorn
- Docker
- Jenkins (CI/CD)
- Pytest & Pylint (testare și calitate cod)

---

## 📂 Structura proiectului

📂 Structura proiectului
```
.
├── n_stanescu.py           # Cod principal Flask
├── requirements.txt         # Biblioteci necesare
├── Dockerfile               # Configurare Docker
├── Jenkinsfile              # Pipeline CI pentru Jenkins
├── app/
│   ├── lib/
│   │   └── helper.py        # Funcții separate pentru conținut
│   └── tests/
│       └── test_n_stanescu.py  # Teste unitare
└── README.md                # Documentație proiect
```

