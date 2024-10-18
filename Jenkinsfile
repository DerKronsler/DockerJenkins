pipeline{
agent { label 'webapp' }
    stages{
        stage("Dependencies"){
        steps{
            sh '''
            USER root
            apk add python3
            apk add py3-pip
            pip install flask
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
