

# Create your views here.


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



from .models import Portfolio
from .serializers import PortSerializer


@method_decorator(csrf_exempt, name='dispatch') 
class EmployeeMain(View):
    
    def get(self, request, *args,**kwargs):
        if request.method=="GET":           
            json_data = request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            id = pythondata.get('id',None)           
        
            if id is not None:
                ris=Portfolio.objects.get(id=id)          
                rishiserialized =PortSerializer(ris) 
                json_data = JSONRenderer().render(rishiserialized.data)
                return HttpResponse(json_data, content_type='application/json')

        #including this because if we not give up a id value to it we just take up all of the objects
        ris = Portfolio.objects.all()
        rishiserialized = PortSerializer(ris, many=True)
        json_data = JSONRenderer().render(rishiserialized.data)
        return HttpResponse(json_data, content_type='application/json')


    def post(self, request,*args,**kwargs):
        if request.method =='POST':
            json_data = request.body    
            stream=io.BytesIO(json_data) #requestbody valued comes into json_data
            pythondata=JSONParser().parse(stream)  #now we require python data so we use json parserer
            ishserializer = PortSerializer(data=pythondata)  #python data to complex object
            if ishserializer.is_valid():                       
                ishserializer.save()                  #after saving we need to send of the response
    
                res ={'msg': 'Data Created------------------------------------------------------------------>'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type ='application/json')
        
#json_data = JSONRenderer().render(serializers.errors) 
        json_data = JSONRenderer().render(ishserializer.errors) 
        return HttpResponse(json_data, content_type ='application/json')


    def put(self, request,*args,**kwargs):
        if request.method == 'PUT': 
            json_data = request.body      
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')        
            emp = Portfolio.objects.get(id=id)
            empserializers = PortSerializer(emp,data=pythondata, partial=True)   
            if empserializers.is_valid():
                empserializers.save()
                resp={'msg': 'Data is now updated with all of the records==================================================>'}
                json_data = JSONRenderer().render(resp)
                return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data, content_type='application/json')


#Now we will give up the update method

    def delete(self, request, *args,**kwargs):
        if request.method == 'DELETE': 
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            de = Portfolio.objects.get(id=id)
            de.delete()  
            flash={'Bot':'Data is been successfully deleted!!'}
            #json_data = JSONRenderer().render(flash)
            #return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(flash, safe=False)