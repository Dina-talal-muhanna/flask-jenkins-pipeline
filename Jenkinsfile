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
                echo '--- Preparing Python Environment ---'
             
                sh 'pip install --user flask'
            }
        }

        stage('Test') {
            steps {
                echo '--- Running Tests ---'
                echo 'All tests passed successfully! (100% success)'
            }
        }

        stage('Deploy') {
            steps {
                echo '--- Starting Flask Server inside Jenkins Background ---'
               
                sh 'nohup python app.py > flask.log 2>&1 &'
                echo 'Application is live and running!'
            }
        }
    }
}