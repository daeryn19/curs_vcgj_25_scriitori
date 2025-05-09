pipeline {
    agent any

    environment {
        VENV_PATH = "./venv"
    }

    stages {
        stage('Build & Setup venv') {
            steps {
                echo 'Setup mediu virtual și instalare dependințe...'
                sh '''
                    python3 -m venv venv
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
                '''
            }
        }

    stage('Pylint - Calitate cod') {
        steps {
        echo 'Rulare pylint pe cod...'
        sh '''
            echo 'Analiză lib/'
            ./venv/bin/pylint --exit-zero lib/

            echo 'Analiză test/'
            ./venv/bin/pylint --exit-zero test/

            echo 'Analiză John_Steinbeck.py'
            PYTHONPATH=app ./venv/bin/pylint --exit-zero John_Steinbeck.py
        '''
    }
}


        stage('Unit Testing') {
            steps {
                echo 'Testare unitară...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    PYTHONPATH=app ./venv/bin/python -m unittest discover -s test

                '''
            }
        }

        stage('Docker Build & Deploy') {
            steps {
                echo "Build Docker pentru John_Steinbeck (ID: ${BUILD_NUMBER})"
                sh '''
                    docker build -t John_Steinbeck:v${BUILD_NUMBER} .
                    docker rm -f John_Steinbeck${BUILD_NUMBER}  true
                    docker create --name John_Steinbeck${BUILD_NUMBER} -p 8020:5000 John_Steinbeck:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}
