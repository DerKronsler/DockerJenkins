pipeline{
agent { label 'webapp' }
    stages{
        stage("Dependencies"){
        steps{
            sh '''
            apk add python3
            apk add py3-pip
            pip install -r requirements.txt
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
