pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[ credentialsId: 'Mohan_GitHub', url: 'https://github.com/mohan-m21/python-3tier-webapp.git' ]]
                )
            }
        }

        // NEW: Install backend dependencies (fixes your pip error)
        stage('Install Backend Dependencies') {
            steps {
                    sh 'cd backend'
                    sh 'pip install -r requirements.txt'
            }
        }

        // NEW: Run backend tests with pytest
        stage('Run Backend Tests') {
            steps {
                dir('backend') {
                    sh 'pytest'  // Assumes you have test files like test_app.py; add them if missing (see Step 3)
                }
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    // OPTIONAL: Add post-build actions (e.g., email on failure)
    post {
        always {
            sh 'docker-compose down'  // Clean up containers after run
        }
        failure {
            echo 'Pipeline failed! Check logs.'
        }
    }
}
