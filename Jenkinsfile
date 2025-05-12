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
        
        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t scriitori:v${BUILD_NUMBER} .
                    docker create --name scriitori${BUILD_NUMBER} -p 8020:5011 scriitori:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
