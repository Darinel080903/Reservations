pipeline{
    agent any
    environment {
        DOCKER_IMAGE = 'service-coso'
        PORT_MAPPING = '8000:8000'
        CONTAINER_NAME = 'service-coso-container'
        AWS_REGION = 'us-east-1'
        AWS_ACCESS_KEY_ID = "${env.AWS_ACCESS_KEY_ID}"
        AWS_SECRET_ACCESS_KEY = "${env.AWS_SECRET_ACCESS_KEY}"
        URR1 = "${env.URR1}"
        USS1 = "${env.USS1}"
        PSS1 = "${env.PSS1}"
    }

    stages {
        stage('Stop Container and Remove') {
            steps {
                script {
                    def containerExists = sh(script: "docker ps -a --filter name=^/${CONTAINER_NAME}\$ --format '{{.Names}}'", returnStdout: true).trim()
                    if (containerExists == CONTAINER_NAME) {
                        sh "docker stop ${CONTAINER_NAME}"
                        sh "docker rm ${CONTAINER_NAME}"
                    }
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    def dockerImage = docker.build(DOCKER_IMAGE)
                    dockerImage.run("-e AWS_ACCESS_KEY_ID=${env.AWS_ACCESS_KEY_ID} \
                        -e AWS_SECRET_ACCESS_KEY=${env.AWS_SECRET_ACCESS_KEY} \
                        -e AWS_REGION=${env.AWS_REGION} \
                        -e URR=${env.URR} \
                        -e USS=${env.USS} \
                        -e PSS=${env.PSS} \
                        -p 8000:8000 --name ${CONTAINER_NAME}")
                }
            }
        }
    }
}