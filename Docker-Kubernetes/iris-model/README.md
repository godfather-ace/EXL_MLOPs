# Iris model Kubernetes tutorial
## Docker Image Building, Tagging and Uploading to Hub

- docker build -t iris-fastapi-service:v1 .

- docker tag iris-fastapi-service:v1 <dockerhub-username>/iris-fastapi-service:v1

- docker push <dockerhub-username>/iris-fastapi-service:v1

## Kubectl command for Deployment

- kubectl create deployment iris-fastapi-service --image=sachin004/iris-fastapi-service:v1 --port=80  

- kubectl expose deployment iris-fastapi-service --type=LoadBalancer --port=80 --target-port=80

- kubectl apply -f C:\Users\sachi\OneDrive\Desktop\AIM\Training\EXL_MLOps\Kubernetes_demo2\iris-classifier-deployment.yaml                                    

- kubectl apply -f C:\Users\sachi\OneDrive\Desktop\AIM\Training\EXL_MLOps\Kubernetes_demo2\iris-classifier-service.yaml                                       

- kubectl get pods  

- kubectl get services

- minikube service iris-predictor-service --url       
