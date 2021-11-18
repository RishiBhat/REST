from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.relations import ManyRelatedField
from rest_framework.views import APIView

# Create your views here.
from .models import Portfolio
from .serializers import HumanSerializer
#including a project for the json from rest_framework.renderers
from rest_framework.renderers import JSONRenderer


#this function was based only on 1 instance
def index(request,pk):
    hm = Portfolio.objects.get(id=pk)   #here we make the object class of our model instance and get gives us the id of the 1st models object
    print("==================================>",hm)
    serializer= HumanSerializer(hm)  # here we just serialized and converted our complex data into python3 data object with this we have to now convert it to the json data              
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++", serializer) 
    print(serializer.data) #this has python3 native data in dict. 
    json_data = JSONRenderer().render(serializer.data)  # now we just converted our native python data into the Json data 
    print("////////////////////////////////////////////////", json_data) #this has the json_data in dict. 

    return HttpResponse(json_data, content_type='application/json')


#this function will be based on the ffull queryset, all portfolio data

def alldt(request):
    hm = Portfolio.objects.all()  
    print(">>>>>>>>",hm)
    serializer= HumanSerializer(hm, many =True) #here we have to give many fields true to take up the wholee queryset to our id               
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<" ,serializer) 
    print(serializer.data)  
    json_data = JSONRenderer().render(serializer.data)  
    print("////////////////////////////////////////////////", json_data)  

    return HttpResponse(json_data, content_type='application/json')


