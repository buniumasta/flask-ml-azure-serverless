# CD-CI - Python Flask Web Framework

This project demonstrates Continuous Integration & Delivery for Python based application using the FLASK Web Framework.

**Sklearn** is used in this project, the Flask Web Application allows to predict the housing prices in Boston based on Kaggle model. The details about the approach can be found at: *[Kaggle Boston](https://www.kaggle.com/c/boston-housing)*, sources for application can be found here.


Project consisted of two phases: Continuous Integration & Continuous delivery, the planning is attached can be seen *[here](https://github.com/buniumasta/flask-ml-azure-serverless/issues/2#issue-780536233)* and tasks were tracked & listed at *[Trello board](https://github.com/buniumasta/flask-ml-azure-serverless/issues/1#issue-780534847)*

## Setting up the stage

Before final Flask Web Application is deployed using CI/CD, it is worth to split activity to smaller tasks and play with simpler examples.
Follwoing will be done:


### Dependencies
1. Create an [Azure Account](https://portal.azure.com)
2. Create an [GitHub](https://github.com/)
3. Basic [Python](https://www.python.org/) knowledge & programming experience
4. Basic shell

Once **Azure** account was created go to portal and login. Open Azure CLI console in portal, see below [screen](https://github.com/buniumasta/flask-ml-azure-serverless/issues/3#issue-780585384)

Go to Github and create repository,

### Create Dummy Python Project

#### Git

Copy HTTPS link of created GitHUB repository from *code* section/tab, clone repository in Azure CLI:

```
git clone <httpslink>
```

Configure global user&email:
```
git config user.name "YourName"
git config user.email "Your@email"
```

Create python files:
*hello.py*
```
def toyou(x):
    return "hi %s" % x


def add(x):
    return x + 1


def subtract(x):
    return x - 1

```

*test_hello.py*
```
from hello import toyou, add, subtract


def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10


def teardown_function(function):
    print("Running Teardown: %s" % function.__name__)
    del function.x


### Run to see failed test
#def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9

```

*is_leap_year.py*
```
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False

    return leap
```


*test_is_leap_year.py*
```
from is_leap_year import is_leap

def test_is_leap_01():
    total=is_leap(1980)
    assert total == True

def test_is_leap_02():
    total=is_leap(2020)
    assert total == True

def test_is_leap_03():
    total=is_leap(1990)
    assert total == False

def test_is_leap_04():
    total=is_leap(2000)
    assert total == True

def test_is_leap_05():
    total=is_leap(2400)
    assert total == True

def test_is_leap_06():
    total=is_leap(2100)
    assert total == False

def test_is_leap_07():
    total=is_leap(2200)
    assert total == False

def test_is_leap_08():
    total=is_leap(2300)
    assert total == False

def test_is_leap_09():
    total=is_leap(2024)
    assert total == True

def test_is_leap_09():
    total=is_leap(24)
    assert total == True

```

Add files to version control, commit and push.
```
git add hello.py
git add test_hello.py
is_leap_year.py
test_is_leap_year.py
git commit -m "dummy project files"
git push
```
Setup & Run Python virtual environment:

```
python3 -m venv ~/.flask-ml-azure
source ~/.flask-ml-azure/bin/activate
```



### Setting up Environment Azure Scaling
