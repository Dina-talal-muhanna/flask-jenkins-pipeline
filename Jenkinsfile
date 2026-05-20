pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                echo '--- Checking out source code ---'
                checkout scm
            }
        }

        stage('Build & Environment Setup') {
            steps {
                echo '--- Setting up Python Environment & Dependencies ---'
                // بنعمل Virtual Environment وبنسطب المكتبات
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo '--- Running Pytest ---'
                // بتشغل التست اللي عملناه بـ pytest
                sh './venv/bin/pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo '--- Deploying Flask Application ---'
                // بنشغل التطبيق في الخلفية على بورت 5000
                sh '''
                fuser -k 5000/tcp || true
                nohup ./venv/bin/python app.py > flask.log 2>&1 &
                '''
                echo 'App deployed successfully!'
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