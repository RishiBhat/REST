from django.shortcuts import render

# Create your views here.
from functools import partial
from django.db.models.fields import DateTimeCheckMixin
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt      
from django.utils.decorators import method_decorator
from django.views import View

#------------------------------------------------------------------------------------------------------------------------------
                                        #now we are just creating the other class based views, so to use class based view we need to import method decorator

from .models import Student
from .serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch') #in order to make the class based view we need to have the namespace as dispatch
class StudentApp(View):
    
    #we get all the CRUD requests operations here
    def get(self, request, *args,**kwargs):
        if request.method=="GET":           
            json_data = request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            id = pythondata.get('id',None)           
        
            if id is not None:
                ris=Student.objects.get(id=id)          #we take up the following id with the GET and take it in the python data
                rishiserialized =StudentSerializer(ris) #takes up all of our data
                json_data = JSONRenderer().render(rishiserialized.data)
                return HttpResponse(json_data, content_type='application/json')

        #including this because if we not give up a id value to it we just take up all of the objects
        ris = Student.objects.all()
        rishiserialized = StudentSerializer(ris, many=True)
        json_data = JSONRenderer().render(rishiserialized.data)
        return HttpResponse(json_data, content_type='application/json')


    def post(self, request,*args,**kwargs):
        if request.method =='POST':
            json_data = request.body    
            stream=io.BytesIO(json_data) #requestbody valued comes into json_data
            pythondata=JSONParser().parse(stream)  #now we require python data so we use json parserer
            ishserializer = StudentSerializer(data=pythondata)  #python data to complex object
            if ishserializer.is_valid():                       
                ishserializer.save()                  #after saving we need to send of the response
                res ={'msg': 'Data Created------------------------------------------------------------------>'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type ='application/json')
        
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data, content_type ='application/json')


    def put(self, request,*args,**kwargs):
        if request.method == 'PUT': 
            json_data = request.body      
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')        
            emp = Student.objects.get(id=id)
            it = StudentSerializer(emp,data=pythondata, partial=True)   

            if it.is_valid():
                it.save()
                resp={'msg': 'Data is now updated with all of the records==================================================>'}
                json_data = JSONRenderer().render(resp)
                return HttpResponse(json_data, content_type='application/json')
            
            json_data = JSONRenderer().render(serializers.Serializer)
            return HttpResponse(json_data, content_type='application/json')


#Now we will give up the update method

    def delete(self, request, *args,**kwargs):
        if request.method == 'DELETE': 
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            de = Student.objects.get(id=id)
            de.delete()  
            flash={'Bot':'Data is been successfully deleted!!'}
            #json_data = JSONRenderer().render(flash)
            #return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(flash, safe=False)
