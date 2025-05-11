```
Proiect: Mihai Eminescu – Prezentare interactivă
Acest proiect este o aplicație web ușoară, dezvoltată cu Flask și containerizată folosind Docker, care oferă o prezentare interactivă a operei lui Mihai Eminescu. 
Include pagini tematice despre biografie, poezie, influențe și manuscrise, fiind integrat într-un proces de livrare continuă (CI/CD) cu Jenkins.

Tehnologii folosite
Python 3.12

Flask

Gunicorn

Docker

Jenkins (CI/CD)

Pytest & Pylint (testare și verificare stil)




.
├── mihai_eminescu.py          # Cod principal Flask
├── requirements.txt           # Biblioteci necesare
├── Dockerfile                 # Configurare Docker
├── Jenkinsfile                # Pipeline CI pentru Jenkins
├── app/
│   ├── lib/
│   │   └── helper.py          # Funcții separate pentru conținut (ex. generare pagini)
│   └── tests/
│       └── test_eminescu.py   # Teste unitare pentru funcționalitate
└── README.md                  # Documentație proiect
 
