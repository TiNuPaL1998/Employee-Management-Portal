pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Application Validation') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python -m py_compile app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t employee-management-portal:latest .
                '''
            }
        }

        stage('List Docker Images') {
            steps {
                sh '''
                    docker images
                '''
            }
        }

        stage('Build Summary') {
            steps {
                echo "Application validation completed successfully."
            }
        }
    }

    post {

        success {
            echo 'Build Successful'
        }

        failure {
            echo 'Build Failed'
        }

        always {
            sh 'rm -rf ${VENV}'
            cleanWs()
            echo 'Pipeline Finished'
        }
    }
}