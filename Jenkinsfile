/*Jenkins*/
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
                    echo '\n\nVerificare biblioteca/*.py cu pylint\n';
                    pylint --exit-zero biblioteca/*.py;

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
                    pytest;
                '''
            }
        }
        /*    }
        }*/
        stage('Deploy') {
            agent any
            steps {
                echo 'IN lucru ! ...'
            }
        }
    }
}
