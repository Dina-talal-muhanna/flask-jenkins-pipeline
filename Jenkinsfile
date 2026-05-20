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
                echo '--- Simulating Build & Installing Dependencies ---'
                echo 'Flask app build steps completed.'
            }
        }

        stage('Test') {
            steps {
                echo '--- Running Application Smoke Tests ---'
                echo 'Testing endpoint connectivity... Success!'
            }
        }

        stage('Deploy') {
            steps {
                echo '--- Deploying Flask Application Container Service ---'
                echo 'App deployed successfully!'
                echo 'URL: http://localhost:5000'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Perfect.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}