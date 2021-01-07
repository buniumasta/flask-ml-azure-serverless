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

Before final Flask Web Application was deployed using CI/CD, it was worth to split activity to smaller tasks and play with simpler examples.

Following 3 main stages were performed:
##### Dummy Python Project & Local Test (python virtual environment)
##### Dummy Python Project & SaaS Build Server - GitHUB
##### FLASK Python WebApplication - Continuous Delivery - Azure Pipelines


## Dummy Python Project & Local Test (python virtual environment)


### Dependencies
1. Create an [Azure Account](https://portal.azure.com)
2. Create an [GitHub](https://github.com/)
3. Basic [Python](https://www.python.org/) knowledge & programming experience
4. Basic shell

**Azure** account need to be created. Storage for Azure CLI need to be reserved, see below [screen](https://github.com/buniumasta/flask-ml-azure-serverless/issues/3#issue-780585384)

Dedicated Github repository needs to be created, this would be the place for the all resources.


#### Git

Repository should be cloned to Azure CLI.

Repository is in sync with GitHub
![Alt text](/img/RepositoryIsCloned.png?raw=true "RepositoryIsCloned")

#### Create Makefile

Makefile structure should be created to enable automation & ensure that all dependencies were installed

Git repo should be up-date with GitHub.

Virtual Python environment should be created and activated.


#### Testing & Checking quality: Dummy Python scripts

Python virtual environment activated and all dependencies installed.

Quality of Code checked & tests were executed for to dummy Python scripts:
![Alt text](/img/testsCont.png?raw=true "Tests")


Make All is executed:
![Alt text](/img/myMake.png?raw=true "RepositoryIsCloned")


## Dummy Python Project & SaaS Build Server - GitHUB

The next phase of the project is to use GitHub environment for execution the tests & code quality check rather than AzureCLI virtual (or Local). For that purpose Git Hub actions needs to be enabled.


GitHub Actions should be enabled and configuration file edited according to needs.

Local repository synchronised with GitHub, and content pushed. Once this done - immediately action should trigger build and Github executes all the magic.

Build should start as presented below:

![Alt text](/img/GitHubBuild.png?raw=true "Build GitHub Actions")

Successful build should look like:

![Alt text](/img/SuccGitHubBuild.png?raw=true "Build GitHub Actions")

##  FLASK Python WebApplication - Continuous Delivery - Azure Pipelines

Azure Pipelines can trigger the build and validate pull request automatically, application then can be automatically deployed.

### Dependencies
1. Githup account
2. An Azure DevOps organisation
3. DevOps project/GitHub Repor


### Instructions

1. GitHub Repository set


2. Repository cloned to Azure Shell & ensure that sklearn files are present


3. Environment setup all decencies installed


5. App service created and initially deployed


6. Deployment verified

```
Check application link:

https://flask-ml-myservice.azurewebsites.net/
```

5. Application verified and checked.

6. Predictions script executed.

Successful prediction in Azure:

![Alt text](/img/SuccessfulPrediction.png?raw=true "Tests")


### Create an Azure DevOps project

Azure DevOps environment configured

  1. New DevOps project named and created
  2. Follow official *[MS documenation](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops)*
  3. New service connection set up with Azure Resource Manager
  4. New Pipeline created
  5. GitHub Integrated
  6. Configuration file Edited.

#### Trigger of Deployment

Every change in source code & push code to Github triggers Deployment of Applicaiton to Azure.

Azure DevOps is triggered:
![Alt text](/img/DevOpsTrigger.png?raw=true "Tests")

Applicaiton Successfully deployed
![Alt text](/img/SuccDeploy.png?raw=true "Tests")

Azure App Service

Application is up & Running, automatically deployed with Name changed:
![Alt text](/img/AppService.png?raw=true "Tests")

10. Logs of application checked

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

Load Statistics looked as followed:
![Alt text](/img/LoadStats.png?raw=true "Tests")

# Enhancements
Consider different languages than Python, customise pipelines.

# Demo
#### Watch short video about the project on *[Youtube](https://youtu.be/abFjDkjCfoQ)*
