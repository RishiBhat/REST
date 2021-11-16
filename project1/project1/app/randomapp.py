import requests

#requesting the url and will be deciding the endpoint of the api

#sending the request

URL = "http://127.0.0.1:8005/stuinfo/1"

#now we will send the get request
#saving the response in r

r =requests.get(url=URL)   #passing the above url

#now extracting the json_data here  

data =r.json(r)
print(data) 
