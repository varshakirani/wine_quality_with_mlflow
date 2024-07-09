# wine_quality_with_mlflow


## How to run?

### Steps to create local virtual environment

```bash
## create conda environment

conda create -n mlflow_project python=3.11 -y
conda activate mlflow_project

## install requirements
pip install -r requirements.txt
````

### Workflow of the code development

Below is the order in which each section of machine learning stage is developed. 

1. Update config.yaml  
2. Update schema.yaml  
3. Update params.yaml  
4. Update the entity  
5. Update the configuration manager in src config  
6. Update the components  
7. Update the pipeline  
8. Update the main.py  
9. Update the app.py 

## MLflow

[MLflow documentation](https://mlflow.org/docs/latest/index.html)  
[dagshub link](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/varshakirani/wine_quality_with_mlflow.mlflow

### Set MLflow credentials from dagshub

Either you can explicitly set the environment variables in terminal by running the below commands
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/varshakirani/wine_quality_with_mlflow.mlflow
export MLFLOW_TRACKING_USERNAME=varshakirani
export MLFLOW_TRACKING_PASSWORD=******
```
Or  
You can update the .env file in the project following the env_template file

## AWS-CICD-Deployment-with-Github-Actions

# Description: About the deployment
```bash
1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2
```
### 1. Login to AWS console.
### 2. Create IAM user for deployment
```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

## 3. Create ECR repo to store/save docker image
```bash
- Save the URI: 652165836244.dkr.ecr.eu-central-1.amazonaws.com/wine_quality
```

### 4. Create EC2 machine (Ubuntu)

### 5. Open EC2 and Install docker in EC2 Machine:
```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
### 6. Configure EC2 as self-hosted runner:
```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

### 7. Setup github secrets:
```bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = eu-central-1

AWS_ECR_LOGIN_URI = demo>>  652165836244.dkr.ecr.eu-central-1.amazonaws.com

ECR_REPOSITORY_NAME = wine_quality
```