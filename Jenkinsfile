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
                python3 index.py
                '''
            }
        }
    
    }
}
