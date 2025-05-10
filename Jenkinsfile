pipeline {
    agent any

    environment {
        IMAGE_NAME = "ion_creanga"
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Preluare cod sursă...'
                checkout scm
            }
        }

        stage('Setup venv și install requirements') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Linter - pylint') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pylint ion_creanga.py || true
                '''
            }
        }

        stage('Unit Tests - pytest') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest tests  # presupune că ai fișiere de test în directorul `tests/`
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Docker Run (opțional)') {
            steps {
                sh '''
                    docker run -d --rm --name creanga_container_${BUILD_NUMBER} -p 5050:5050 ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo 'Build, test și dockerizare reușite.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}
