pipeline{
agent { label 'master' }
    triggers{
        pollSCM '* * * * *' 
    } 
    stages{
        stage("Dependencies"){
        steps{
            sh '''
            apt install python3
            apt install py3-pip
            apt install py3-flask
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
