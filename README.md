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


---

## Functionalitati
![image](https://github.com/user-attachments/assets/bc731760-e876-43e4-a2d7-db5bd773f28f)


## Exemple pagină web

### Pagina principală  
![image](https://github.com/user-attachments/assets/ad23729a-66f3-4efe-b3b8-fcaf0c015483)

### Pagina scriitorului Victor Hugo  
![image](https://github.com/user-attachments/assets/41ec16f1-1ebd-4236-84e2-28d1b91074ba)

### Descriere scriitor  
![image](https://github.com/user-attachments/assets/94e8dbda-d2a9-4be0-9697-16bdc5a6cda8)


### Opere reprezentative  
![image](https://github.com/user-attachments/assets/c0ecd69a-847a-461e-9b06-8ece0f33375b)

---

## Testare cu pytest

Rulare teste:

```bash
pytest
```
![image](https://github.com/user-attachments/assets/02667f44-129e-4466-8a13-1d9415b97241)


---


## Docker

### Creare imagine, container si rulare:

```bash
sudo docker build -t scriitori_victor_hugo .
```

![image](https://github.com/user-attachments/assets/2bfcddd4-2d23-42cc-ace6-e1046794d078)
![image](https://github.com/user-attachments/assets/d753b975-6de8-47ab-97d9-a62ee559c549)

### Imagini existente:

```bash
docker images
```
![image](https://github.com/user-attachments/assets/a69fe114-e508-4a9e-a4f0-1a29c440b239)

### Containere existente:

```bash
sudo docker ps -a
```
![image](https://github.com/user-attachments/assets/410a5ead-2d84-41d8-953c-62baef1651e7)

### Oprire container:

```bash
sudo docker stop epic_hawking
```
### Stergere imagine si container:

```bash
sudo docker rmi scriitori_victor_hugo
sudo docker rm epic_hawking
```


---

## DevOps CI

### Pipeline Jenkins
- Fișierul `Jenkinsfile` conține pașii pentru testare și build.
- Este configurat cu un pipeline declarativ.

```bash
pipeline {
    agent any

    stages {

        stage('Instalare dependințe') {
            steps {
                echo 'Se instaleaza dependintele...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Testare') {
            steps {
                echo 'Se rulează testele...'
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }
    }

    post {
        success {
            echo 'Build finalizat cu succes!'
        }
        failure {
            echo 'Build eșuat!'
        }
    }
}
```

## Bibliografie

- [Python](https://docs.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pytest](https://docs.pytest.org/)
- [Docker](https://www.docker.com/)
- [Jenkins](https://www.jenkins.io/)
- [Proiect SCC GitHub (exemplu)](https://github.com/crchende/sysinfo)
