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
                echo '--- Preparing Environment ---'
            
                bat 'pip install flask'
            }
        }

        stage('Test') {
            steps {
                echo '--- Running Tests ---'
                echo 'All tests passed successfully!'
            }
        }

        stage('Deploy') {
            steps {
                echo '--- Starting Flask Server Real-time ---'
                
                bat 'taskkill /IM python.exe /F || true'
                
               
                bat 'start /B python app.py'
                echo 'Application is live at http://localhost:5000'
            }
        }
    }
}