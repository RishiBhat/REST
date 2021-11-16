from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.relations import ManyRelatedField

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
#including a project for the json from rest_framework.renderers
from rest_framework.renderers import JSONRenderer

# Create your views here.

def stuinfo(request, pk):
    hm = Student.objects.get(id=pk)   #here we make the object class of our model instance and get gives us the id of the 1st models object
    print("==================================>",hm)
    serializer= StudentSerializer(hm)  # here we just serialized and converted our complex data into python3 data object with this we have to now convert it to the json data              
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++", serializer) 
    print(serializer.data) #this has python3 native data in dict. 

    #json_data = JSONRenderer().render(serializer.data)  # now we just converted our native python data into the Json data 
    #print("////////////////////////////////////////////////", json_data) #this has the json_data in dict. 
    #return HttpResponse(json_data, content_type='application/json')
    return  JsonResponse(serializer.data, safe=True)  #safe is not mandatory as we can see the views in json_data format as well..
    #safe method default takes true value...
    #here safe returns us the data in dict format


def tsk(request):
    hm = Student.objects.all()  
    print(">>>>>>>>",hm)
    serializer= StudentSerializer(hm, many =True) #here we have to give many fields true to take up the whole queryset to our id               
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<" ,serializer) 
    print(serializer.data)  
    json_data = JSONRenderer().render(serializer.data)  
    #print("////////////////////////////////////////////////", json_data)  
    #return HttpResponse(json_data, content_type='application/json') #here if we keep safe=true it will not work because the data is in non-dict form
    return JsonResponse(serializer.data, safe=False)



    