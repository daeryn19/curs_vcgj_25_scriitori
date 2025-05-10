pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Se instalează dependințele...'
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Test') {
            steps {
                echo 'Nu există teste automate definite.'
            }
        }

        stage('Run app') {
            steps {
                echo 'Pornim aplicația Flask...'
                sh 'python3 app/scriitori_baston.py & sleep 5'
            }
        }
    }
}
