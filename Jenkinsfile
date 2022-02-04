node {
    stage('Stop and Delete Container') {
        sh 'docker rm -f casestudy'
    }
    stage('Delete Image') {
        sh 'docker image rm -f mustafatirnova/bcfmcasestudy:latest'
    }
    stage('Pull Image') {
        sh 'docker pull mustafatirnova/bcfmcasestudy:latest'
    }
    stage('Run Container') {
        sh 'docker run --name casestudy -d -p 80:5000 --env API_KEY=apikeyvalue mustafatirnova/bcfmcasestudy:latest'
    }
}

