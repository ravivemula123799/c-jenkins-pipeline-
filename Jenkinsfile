pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/c-jenkins-pipeline.git'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python build_and_run.py'
            }
        }

        stage('Archive Output') {
            steps {
                archiveArtifacts artifacts: 'hello.exe', onlyIfSuccessful: true
            }
        }
    }
}
