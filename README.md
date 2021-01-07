# Overview

## CD-CI - Python Flask Web Framework

![Python application test with Github Actions](https://github.com/buniumasta/flask-ml-azure-serverless/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

[![Build Status](https://dev.azure.com/bartoszpostrowski/flask-ml-azure-serverless/_apis/build/status/buniumasta.flask-ml-azure-serverless?branchName=main)](https://dev.azure.com/bartoszpostrowski/flask-ml-azure-serverless/_build/latest?definitionId=2&branchName=main)

This project demonstrates Continuous Integration & Delivery for Python based application using the FLASK Web Framework. Architecture of solution is presented below:
![Alt text](/img/architecture.png?raw=true "Architecture")

**Sklearn** is used in this project, the Flask Web Application allows to predict the housing prices in Boston based on Kaggle model. The details about the approach can be found at: *[Kaggle Boston](https://www.kaggle.com/c/boston-housing)*, sources for application can be found [here](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/tree/master/C2-AgileDevelopmentwithAzure/project/starter_files)

#### Watch short video about the project on *[Youtube](https://youtu.be/abFjDkjCfoQ)*

# Project Plan

Project consisted of two phases: Continuous Integration & Continuous delivery, the planning is attached can be seen *[here](https://github.com/buniumasta/flask-ml-azure-serverless/issues/2#issue-780536233)* and tasks were tracked & listed at *[Trello board](https://github.com/buniumasta/flask-ml-azure-serverless/issues/1#issue-780534847)*

# Instructions

Before final Flask Web Application is deployed using CI/CD, it is worth to split activity to smaller tasks and play with simpler examples.
Following will be done:
##### Dummy Python Project & Local Test (python virtual environment)
##### Dummy Python Project & SaaS Build Server - GitHUB
##### FLASK Python WebApplication - Continuous Delivery - Azure Pipelines


## Dummy Python Project & Local Test (python virtual environment)


### Dependencies
1. Create an [Azure Account](https://portal.azure.com)
2. Create an [GitHub](https://github.com/)
3. Basic [Python](https://www.python.org/) knowledge & programming experience
4. Basic shell

Once **Azure** account was created go to portal and login. Open Azure CLI console in portal, see below [screen](https://github.com/buniumasta/flask-ml-azure-serverless/issues/3#issue-780585384)

Go to Github and create repository,


#### Git

Copy SSH link of created GitHUB repository from *code* section/tab, clone repository in Azure CLI, ensure that it is up to date:

Repository is in sync with GitHub
![Alt text](/img/RepositoryIsCloned.png?raw=true "RepositoryIsCloned")

#### Create Makefile

Add basic Makefile structure to enable automation & ensure that all dependencies is installed

Add files to git version control, commit and push.

Setup & Run Python virtual environment:


#### Testing & Checking quality: Dummy Python scripts

Prepare environment by installing Dependencies

Check quality of Code (lint) & Run tests for to dummy Python scripts:
![Alt text](/img/testsCont.png?raw=true "Tests")


Make All is executed:
![Alt text](/img/myMake.png?raw=true "RepositoryIsCloned")


## Dummy Python Project & SaaS Build Server - GitHUB

The next phase of the project is to use GitHub environment for execution the tests & code quality check. For that purpose Git Hub actions needs to be enabled.


Using Git hub portal go to Actions and define your own, and add following content to main.yml:

```
# This is a basic workflow to help you get started with Actions
name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.5
      uses: actions/setup-python@v1
      with:
        python-version: 3.5
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint_hello
        make lint_is_leap
    - name: Test with pytest
      run: |
        make test_hello
        make test_is_leap

```

Synchronise your local repository with github, and push content. This action should trigger build and Github will do magic for you.

Build will start as presented below:

![Alt text](/img/GitHubBuild.png?raw=true "Build GitHub Actions")

Successful build will look like:

![Alt text](/img/SuccGitHubBuild.png?raw=true "Build GitHub Actions")

##  FLASK Python WebApplication - Continuous Delivery - Azure Pipelines

Azure Pipelines can trigger the build and validate pull request automatically

### Dependencies
1. Githup account
2. An Azure DevOps organisation
3. DevOps project/GitHub Repor


### Instructions

1.  Set Up Your GitHub Repository,


2. Clone the Repository & ensure that sklearn files are present


```
git clone <(ssh link from github)>
```

3. Set up virtualenv:

```
python3 -m venv ~/.flask-ml-azure
source ~/.flask-ml-azure/bin/activate
```

4. Run make install & install dependencies

5.  Create an app service and initially deploy your app in Cloud Shell:

```
az webapp up -n flask-ml-myservice
```

6. Verify the deployed application works by browsing to the deployed url

```
Check application link:

https://flask-ml-myservice.azurewebsites.net/
```

5. Edit Shell script make_predict_azure_app.sh

```
Change the line in make_predict_azure_app.sh to match the deployed prediction:
-X POST https://flask-ml-myserice.azurewebsites.net:$PORT/predict
```

6. Run prediction prediction script and feed in application with example data.

Successful prediction in Azure will look like:

![Alt text](/img/SuccessfulPrediction.png?raw=true "Tests")


### Create an Azure DevOps project
Next, we'll need to create an Azure DevOps project and connect to Azure.

  1. Create new project and name it
  2. Follow official *[MS documenation](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops)*
  3. Setup  new service connection with Azure Resource Manager
  4. Select Pipeline and create a new one.
  5. Create the GitHub Integration and choose Configure Python to Linux Web App on Azure
  6. Edit YAML file as follow:

```
# Python to Linux Web App on Azure
# Build your Python project and deploy it to Azure as a Linux Web App.
# Change python version to one thats appropriate for your application.
# https://docs.microsoft.com/azure/devops/pipelines/languages/python

trigger:
- main

variables:
  # Azure Resource Manager connection created during pipeline creation
  azureServiceConnectionId: 'a2871cdf-a404-4080-9125-973b64a3c2a5'

  # Web app name
  webAppName: 'flask-ml-myservice'

  # Agent VM image name
  vmImageName: 'ubuntu-latest'

  # Environment name
  environmentName: 'flask-ml-myservice'

  # Project root folder. Point to the folder containing manage.py file.
  projectRoot: $(System.DefaultWorkingDirectory)

  # Python version: 3.7
  pythonVersion: '3.7'

stages:
- stage: Build
  displayName: Build stage
  jobs:
  - job: BuildJob
    pool:
      vmImage: $(vmImageName)
    steps:
    - task: UsePythonVersion@0
      inputs:
        versionSpec: '$(pythonVersion)'
      displayName: 'Use Python $(pythonVersion)'

    - script: |
        python -m venv antenv
        source antenv/bin/activate
        python -m pip install --upgrade pip
        pip install setup
        pip install -r requirements.txt
      workingDirectory: $(projectRoot)
      displayName: "Install requirements"

    - script: |
        python -m venv antenv
        source antenv/bin/activate
        make install
        make lint
      workingDirectory: $(projectRoot)
      displayName: "Run Lint test"

    - task: ArchiveFiles@2
      displayName: 'Archive files'
      inputs:
        rootFolderOrFile: '$(projectRoot)'
        includeRootFolder: false
        archiveType: zip
        archiveFile: $(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip
        replaceExistingArchive: true

    - upload: $(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip
      displayName: 'Upload package'
      artifact: drop

- stage: Deploy
  displayName: 'Deploy Web App'
  dependsOn: Build
  condition: succeeded()
  jobs:
  - deployment: DeploymentJob
    pool:
      vmImage: $(vmImageName)
    environment: $(environmentName)
    strategy:
      runOnce:
        deploy:
          steps:

          - task: UsePythonVersion@0
            inputs:
              versionSpec: '$(pythonVersion)'
            displayName: 'Use Python version'

          - task: AzureWebApp@1
            displayName: 'Deploy Azure Web App : flask-ml-myservice'
            inputs:
              azureSubscription: $(azureServiceConnectionId)
              appName: $(webAppName)
              package: $(Pipeline.Workspace)/drop/$(Build.BuildId).zip

```

8. Make the change in application & push code to Github -> Deployment process should start.

Go to Azure DevOps and check the if was triggered:
![Alt text](/img/DevOpsTrigger.png?raw=true "Tests")

Successful deployment will look like
![Alt text](/img/SuccDeploy.png?raw=true "Tests")

9. Azure App Service

Application is up & Running, it was successfully deployed with Name changed:
![Alt text](/img/AppService.png?raw=true "Tests")

10. Check logs of Application

```
az webapp log tail --name flask-ml-myservice --resource-group <YOURRG>

```


```
Ending Log Tail of existing logs ---

Starting Live Log Stream ---

2021-01-06T18:12:18.435851738Z [2021-01-06 18:12:18,434] INFO in app: JSON payload: %s json_payload
2021-01-06T18:12:18.441159543Z [2021-01-06 18:12:18,440] INFO in app: inference payload DataFrame: %s inference_payload
2021-01-06T18:12:18.441876443Z [2021-01-06 18:12:18,441] INFO in app: Scaling Payload: %s payload
2021-01-06T18:12:18.452119652Z 172.16.0.1 - - [06/Jan/2021:18:12:18 +0000] "POST /predict HTTP/1.1" 200 35 "-" "curl/7.64.0"
```
11. LoadTest Executution

Load was generated and application stability was checked:
![Alt text](/img/LoadTests.png?raw=true "Tests")

# Enhancements
Consider different languages than Python, customise pipelines.

# Demo
#### Watch short video about the project on *[Youtube](https://youtu.be/abFjDkjCfoQ)*
