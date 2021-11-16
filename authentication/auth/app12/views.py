from django.shortcuts import render
from rest_framework import authentication
from rest_framework.decorators import authentication_classes, permission_classes

# Create your views here.


from app12.models import Student
from app12.serializers import StudentSerialzer
from rest_framework import viewsets 
from rest_framework.authentication import BasicAuthentication   
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
#modelSetView in CRUD operation




class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    
    #This is for any type of user
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]





#This is gives us the basic API

