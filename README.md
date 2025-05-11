# curs_vcgj_25_scriitori

Aplicație educațională despre scriitori români – Mihail Sadoveanu.

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

Aplicația **Scriitori** este o aplicație web simplă, realizată cu Flask, care oferă informații despre viața și opera scriitorului **Mihail Sadoveanu**.

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
git clone -b devel_guramba_elena https://github.com/daeryn19/curs_vcgj_25_scriitori.git
cd curs_vcgj_25_scriitori
```

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

![image](https://github.com/user-attachments/assets/2c0f2e67-7d07-41aa-bb62-e3c2d7d84611)


## Exemple pagină web

### Pagina principală  
![image](https://github.com/user-attachments/assets/b9ed2d07-7f86-46d9-8150-856dc49726c4)


### Pagina scriitorului Mihail Sadoveanu  
![image](https://github.com/user-attachments/assets/b0b428fb-9959-45f1-93c0-be5100ef1000)


### Descriere scriitor  
![image](https://github.com/user-attachments/assets/01295832-c4b1-4f18-ada5-beae17114c7f)


### Opere reprezentative  
![image](https://github.com/user-attachments/assets/e274cd52-4b88-4e71-b344-483ff0a12566)


---

## Testare cu pytest

Rulare teste:

```bash
pytest
```

![image](https://github.com/user-attachments/assets/65b4e64c-8f9c-4c9a-959e-86204eb3d41a)


---


## Docker

### Creare imagine, container si rulare:

```bash
chmod +x creare_imagine_si_container.sh
./creare_imagine_si_container.sh
```

![image](https://github.com/user-attachments/assets/d5b55467-aebb-40ca-a6ad-49437b1fc728)


### Imagini existente:

```bash
docker images
```

![image](https://github.com/user-attachments/assets/dfbb2635-c500-49de-9b81-6ce0175a5708)


### Containere existente:

```bash
docker ps -a
```

![image](https://github.com/user-attachments/assets/dafe6d56-70e0-4f26-93f6-7b180b71add9)


### Oprire container:

```bash
docker stop scriitori_elena_container
```

### Stergere imagine si container:

```bash
chmod +x stergere_container_si_imagine.sh
./stergere_container_si_imagine.sh
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

![image](https://github.com/user-attachments/assets/4cfdb28f-de85-412c-9a6e-5749d062d6d4)


![image](https://github.com/user-attachments/assets/62cf65c6-2d06-4806-a791-d14bbdb5021e)


---

## Bibliografie

- [Python](https://docs.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pytest](https://docs.pytest.org/)
- [Docker](https://www.docker.com/)
- [Jenkins](https://www.jenkins.io/)
- [Proiect SCC GitHub (exemplu)](https://github.com/crchende/sysinfo)
