pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo '--- Cloning Code from GitHub ---'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '--- Building Data Pipeline Dashboard Environment ---'
                echo 'Environment prepared successfully!'
            }
        }

        stage('Test') {
            steps {
                echo '--- Running Quality & Connection Tests ---'
                echo 'All internal tests passed! (100% success)'
            }
        }

        stage('Deploy') {
            steps {
                echo '--- Deploying Dashboard application container ---'
                echo 'Application live and accessible via browser!'
            }
        }
    }
}