pipeline{
agent { label 'webapp' }
    stages{
        stage("Dependencies"){
        steps{
            sh '''
            apt install python3
            apt install py3-pip
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
