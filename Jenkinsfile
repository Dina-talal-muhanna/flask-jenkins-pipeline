pipeline {
    agent any

    options {
        
        skipDefaultCheckout()
    }

    environment {
        IMAGE_NAME = 'flask-app'
        CONTAINER_NAME = 'flask-running'
    }

    stages {
        stage('Clone') {
            steps {
                echo '--- Cloning Code from GitHub ---'
               
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '--- Building Docker Image ---'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Test') {
            steps {
                echo '--- Running Unit Tests inside Docker ---'
                sh "docker run --rm ${IMAGE_NAME} pytest test_app.py"
            }
        }

        stage('Deploy') {
            steps {
                echo '--- Deploying Container ---'
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
                echo "App deployed at http://localhost:5000"
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! App is running.'
        }
    }
}