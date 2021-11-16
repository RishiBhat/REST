import requests
import json

#Reminder:: This can be any any third party application, so it is just for the testing purpose which we use over here

URL= " http://127.0.0.1:8000/es"


def get_data(id=None):     
    data={}                         
    if id is not None:            
        data={'id':id}     
    json_data = json.dumps(data)       
    r=requests.get(url=URL, data=json_data)
    data=r.json()                  
    print(data) 

#get_data()


def post_data():
    data = {
       'name':'Gopal',
       'roll':20,
       'city': 'nagasakhi'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
#post_data()


# now will update the above details so commented the post_data() fx()

def update_data():

    data = {
        
        #we need to provide the ID if we wanna update the required value
        'id':4,
        'name':'Sakura',
        'city':'Konuha', 
        'roll':500
    }
   
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)    #in update we have put request & read we have the post request
    data = r.json()
    print(data)
#update_data()

#now we will perform the delete data 

def delete_data():
    data ={ 'id': 7}     #now we just need to give the specific ID to delete the data we do not require in our db....
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)    #Now we use the delete request to del. the specific record from our db...
    data = r.json()
    print(data)

delete_data()