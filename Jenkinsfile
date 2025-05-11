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
                echo 'Rulare pylint pe codul popa_adrian_scriitori...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo 'Analiză lib/.py'
                    pylint --exit-zero lib/.py  true

                    echo 'Analiză test/.py'
                    pylint --exit-zero test/.py  true

                    echo 'Analiză popa_adrian_scriitori.py'
                    pylint --exit-zero popa_adrian_scriitori.py  true
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
                echo "Build Docker pentru popa_adrian_scriitori (ID: ${BUILD_NUMBER})"
                sh '''
                    docker build -t popa_adrian_scriitori:v${BUILD_NUMBER} .
                    docker rm -f popa_adrian_scriitori${BUILD_NUMBER}  true
                    docker create --name popa_adrian_scriitori${BUILD_NUMBER} -p 8020:5000 popa_adrian_scriitori:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline scriitori finalizat cu succes.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}