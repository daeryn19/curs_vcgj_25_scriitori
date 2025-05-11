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

