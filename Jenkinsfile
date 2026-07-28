pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code downloaded successfully.'
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Pip Version') {
            steps {
                bat 'pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Application Check') {
            steps {
                bat 'python app.py --help'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished.'
        }

        success {
            echo 'Pipeline Completed Successfully.'
        }

        failure {
            echo 'Pipeline Failed.'
        }
    }
}


