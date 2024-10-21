pipeline{
agent { label 'webapp' }
    triggers{
        pollSCM '* * * * *' 
    } 
    stages{
        stage("Dependencies"){
        steps{
            sh '''
            apk add python3
            apk add py3-pip
            apk add py3-flask
            '''

             }
        
        }
        stage("Testen"){
            steps{
                sh '''
                cd web
                python index.py &
                '''
            }
        }
        stage("Git Add"){
            steps{
                sh '''
                mv web/index.py final
                ls
                cd final
                git add index.py
                git commit -m 'Add testfile from Jenkins Pipeline'
                git branch -a
                '''
                
            }
        }
        stage("Push"){
            steps{
                withCredentials([gitUsernamePassword(credentialsId: 'derkronsler-githubtoken', gitToolName: 'Default')]) {
                sh "git push origin main" 
                }
            }
        }
    }
}
