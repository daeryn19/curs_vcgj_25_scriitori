pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'frankherbert2'  // Numele imaginii Docker
        DOCKER_TAG = 'latest'  // Tag-ul imaginii
    }

    stages {
        stage('Checkout') {
            steps {
                // Clonăm repo-ul și branch-ul de care avem nevoie
                git branch: 'devel_cazanaru_radu', url: 'https://github.com/daeryn19/curs_vcgj_25_scriitori.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Construim imaginea Docker folosind Dockerfile-ul
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Dacă ai testele, le poți rula aici
                    // sh 'docker run --rm $DOCKER_IMAGE:$DOCKER_TAG python -m unittest discover -s tests'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Rulăm containerul cu aplicația ta Flask
                    sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }
    }

    post {
        always {
            // Curățăm sistemul de imagini nefolosite după execuția pipeline-ului
            sh 'docker system prune -f'
        }
    }
}

