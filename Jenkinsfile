pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'devel_cazanaru_radu', url: 'https://github.com/daeryn19/curs_vcgj_25_scriitori.git'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t frankherbert2 .'
            }
        }

        stage('Run Docker container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name frankherbert_container frankherbert2'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

