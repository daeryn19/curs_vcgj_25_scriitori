pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    ls -l /var/lib/jenkins/workspace/${JOB_NAME}	
                    cd app;
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                '''
            }
        }
	/*
         stage('Testare') {
              problema rulare in paralel, al doilea stage nu mai poate porni venv-ul
             parallel {
                 stage('Paralel 1') {
                    steps {
                        echo 'Test 1'
                     }
                 }
                stage('Paralel 2') {
                     steps {
                         echo 'Test 2'
                    }
                 }
            }
         }
	*/
        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    cd app;
                    . ./activeaza_venv;
                    echo '\n\nVerificare lib/*.py cu pylint\n';
                    pylint --exit-zero lib/*.py;
                    echo '\n\nVerificare tests/*.py cu pylint';
                    pylint --exit-zero tests/*.py;
                    echo '\n\nVerificare 445D_scriitori.py cu pylint';
                    pylint --exit-zero 445D_scriitori.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    cd app;
                    . ./activeaza_venv;
                    python3 -m pytest -v;
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'IN lucru ! ...'
            }
        }
    } // <- Închide blocul "stages"
} // <- AICI era paranteza LIPSĂ: închiderea blocului "pipeline"

