pipeline {
    agent any

    environment {
        VENV="./activeaza_venv_jenkins"
    }

    stages {
        stage('Build') {
            steps {
                echo ' Build - Activare virtualenv și listare fișiere'
                sh '''
                    pwd
                    ls -l
                    . ${VENV}
                '''
            }
        }

        stage('Calitate cod - pylint') {
            steps {
                echo ' Verificare calitate cod cu pylint'
                sh '''
                    . ${VENV}
                    echo 'Verificare app/libs/*.py'
                    pylint --exit-zero app/libs/*.py || true

                    echo 'Verificare app/tests/*.py'
                    pylint --exit-zero app/tests/*.py || true

                    echo 'Verificare app/443D_scriitori.py'
                    pylint --exit-zero app/443D_scriitori.py || true
                '''
            }
        }

        stage('Unit Testing - pytest') {
            steps {
                echo ' Rulare teste unitare cu pytest'
                sh '''
                    . ${VENV}
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo ' Deploy (în lucru)'
            }
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt || true'
                sh 'pytest'
            }
        }
    }
}
