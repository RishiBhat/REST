from django.http import response
from django.shortcuts import render

# Create your views here.

#first we will require to send the 3rd party application 

#function based api view we will do here 

from rest_framework.decorators import api_view
from rest_framework.response import Response                                   #This is the Response which we get in the function based api_view
from rest_framework.reverse import reverse


#@api_view(['GET'])                                                  #If we use the GET as it will work as the same bc it has the default method GET
#by default th get method is present over here

#def hello_world(request):
 #   return Response({'msg':'Hello World'})              #This is the python native dictionary stored  here


@api_view(['GET','POST'])

def hello_world(request):
    if request.method == 'GET':
        return response({'BOT':'This is the GET method activated++++++++++++++++++++++++++++++++++++++', 'data':request.data})
    
    if request.method=='POST':                     #if this is the POST method we have to check it explicitly
        print(request.data)                 #will get to know what lies within the data, as you can see on the server the data which we get is the parsed data. 
        return Response({'msg': 'This is the post method activated==========================> ','data':request.data})
#including the get and post within 1 function
#in our 3rd  party app we have not defined the content type so we get a error as {'detail': 'Unsupported media type "text/plain" in request.'}, therefore just defining the 
#content type in 3rd app