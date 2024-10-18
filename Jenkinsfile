pipeline{
agent { label 'webapp' }
    stages{
        stage("Dependencies"){
        steps{
            sh '''
            apk add python3
            apk add py3-pip
            python3 -m venv .venv
            source .venv/bin/activate
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
