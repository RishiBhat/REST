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
from .models import Emp
from .serializers import EmpSerializers
from .serializers import *
from rest_framework import *



@method_decorator(csrf_exempt, name='dispatch') 
class EsMain(View):
    def get(self, request, *args,**kwargs):
        if request.method=="GET":           
            json_data = request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            id = pythondata.get('id',None)           
            if id is not None:
                ris=Emp.objects.get(id=id)          
                rishiserialized =EmpSerializers(ris) 
                json_data = JSONRenderer().render(rishiserialized.data)
                return HttpResponse(json_data, content_type='application/json')

        
            ris = Emp.objects.all()
            rishiserialized = EmpSerializers(ris, many=True)
            json_data = JSONRenderer().render(rishiserialized.data)
            return HttpResponse(json_data, content_type='application/json')


    def post(self, request,*args,**kwargs):
        if request.method =='POST':
            json_data = request.body    
            stream=io.BytesIO(json_data) 
            pythondata=JSONParser().parse(stream)
            ishserializer = EmpSerializers(data=pythondata)

            if ishserializer.is_valid():                       
                ishserializer.save()                 
                res ={'msg': 'Data Created------------------------------------------------------------------>'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type ='application/json')
        json_data = JSONRenderer().render(serializers.Serializer)
        return HttpResponse(json_data, content_type ='application/json')


    def put(self, request,*args,**kwargs):
        
        if request.method == 'PUT': 
            json_data = request.body      
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')        
            emp = Emp.objects.get(id=id)
            EmpSerializers = EmpSerializers(emp,data=pythondata, partial=True)   

            if EmpSerializers.is_valid():
                EmpSerializers.save()
                resp={'msg': 'Data is now updated with all of the records==================================================>'}
                json_data = JSONRenderer().render(resp)
                return HttpResponse(json_data, content_type='application/json')

            json_data = JSONRenderer().render(serializers.errors)
            return HttpResponse(json_data, content_type='application/json')



    def delete(self, request, *args,**kwargs):
        
        if request.method == 'DELETE': 
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            de = Emp.objects.get(id=id)
            de.delete()  
            flash={'Bot':'Data is been successfully deleted!!'}
            return JsonResponse(flash, safe=False)
