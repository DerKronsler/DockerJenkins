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
            apk add py3-mock
            pip install Python-IO
            '''

             }
        
        }
        stage("Testen"){
            steps{
                sh '''
                python -m unittest test_rpggame.py
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
                sh "git push origin HEAD:main" 
                }
            }
        }
    }
}
