pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Mohan_GitHub', url: 'https://github.com/mohan-m21/python-3tier-webapp.git']])
            }
        }
        stage('installing pytest') {
            steps {
                sh 'pip install pytest'
                sh 'pytest'
            }
        }
        stage('building') {
            steps {
                sh 'pip install -m build'
                sh 'build'
            }
        }
        stage('image building') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${TAG}'
            }
        }
    }
}

