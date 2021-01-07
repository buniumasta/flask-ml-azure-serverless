from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    @task(1)
    def hello_world(self):
        self.client.post("https://flask-ml-myservice.azurewebsites.net:443/predict", {
           "CHAS":{
              "0":0
           },
           "RM":{
              "0":6.575
           },
           "TAX":{
              "0":296.0
           },
           "PTRATIO":{
              "0":15.3
           },
           "B":{
              "0":396.9
           },
           "LSTAT":{
              "0":4.98
           }
        })

    @task(2)
    def index(self):
        self.client.get("https://flask-ml-myservice.azurewebsites.net/index")
