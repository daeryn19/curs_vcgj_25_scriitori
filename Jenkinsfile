pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv;
                    echo '\n\nVerificare libs/*.py cu pylint\n';
                    pylint --exit-zero libs/*.py;

                    echo '\n\nVerificare tests/*.py cu pylint';
                    pylint --exit-zero tests/*.py;

                    echo '\n\nVerificare scriitori.py cu pylint';
                    pylint --exit-zero scriitori.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv;
                    flask --app scriitori test;
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t scriitori:v${BUILD_NUMBER} . 
                    docker create --name scriitori${BUILD_NUMBER} -p 8020:5000 scriitori:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
