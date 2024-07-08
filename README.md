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