pipeline {
    agent any

    stages {
        // Etapa 1 - Build
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    # Afișare director curent și listare fișiere
                    pwd;
                    ls -l;

                    # Activare venv și instalare dependențe
                    . ./activeaza_venv_jenkins;
                '''
            }
        }

        // Etapa 2 - Calitate Cod cu Pylint
        stage('Pylint - Calitate Cod') {
            steps {
                echo 'Verificare calitate cod cu Pylint...'
                sh '''
                    # Activare venv
                    . ./activeaza_venv;

                    # Verificare cod din directoarele app/libs și app
                    echo '\n\nVerificare libs/*.py cu pylint\n';
                    pylint --exit-zero app/libs/*.py;

                    echo '\n\nVerificare victor_hugo.py cu pylint';
                    pylint --exit-zero app/victor_hugo.py;
                '''
            }
        }

        // Etapa 3 - Testare Unitara cu Pytest
        stage('Unit Testing cu Pytest') {
            steps {
                echo 'Rulează testele unitare...'
                sh '''
                    # Activare venv
                    . ./activeaza_venv;

                    # Rulare teste din directorul tests/
                    pytest tests/;
                '''
            }
        }

        // Etapa 4 - Docker Build și Deploy
        stage('Docker Build și Deploy') {
            steps {
                echo "Creare imagine docker și deploy"
                sh '''
                    # Creare imagine Docker
                    docker build -t victor_hugo:v${BUILD_NUMBER} .

                    # Creare container cu imaginea nouă
                    docker create --name victor_hugo_${BUILD_NUMBER} -p 8020:5011 victor_hugo:v${BUILD_NUMBER}
                '''
            }
        }
    }
}

