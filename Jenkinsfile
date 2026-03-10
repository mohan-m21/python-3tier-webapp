pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Mohan_GitHub', url: 'https://github.com/mohan-m21/python-3tier-webapp.git']])
            }
        }
        stage('image building') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${TAG}'
            }
        }
        stage('Deploy Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}

