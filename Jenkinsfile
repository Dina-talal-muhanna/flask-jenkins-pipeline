pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                echo '--- Checking out source code ---'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '--- Building Docker Image ---'
                sh 'docker build -t flask-app .'
            }
        }

        stage('Test') {
            steps {
                echo '--- Running Tests inside Docker Container ---'
                sh 'docker run --rm flask-app pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo '--- Deploying container ---'
                sh '''
                docker stop flask-running || true
                docker rm flask-running || true
                docker run -d --name flask-running -p 5000:5000 flask-app
                '''
                echo 'App deployed successfully at http://localhost:5000'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! App is running.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}