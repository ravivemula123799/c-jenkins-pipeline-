pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ravivemula123799/c-jenkins-pipeline-.git'  
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
