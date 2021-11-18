from django.shortcuts import render
from rest_framework import permissions

# Create your views here.
from app30.models import Student
from app30.serializers import StudentSerializer
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from app30.throttling import risThrottle


class fc(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permissions_classes = [IsAuthenticatedOrReadOnly] 
    throttle_classes = [AnonRateThrottle, risThrottle] #The rate for the anon user will be configured in the settings.py file

    #if you wanna use the anon rate(throttle) in other classes just keep inheriting this as [PARENT CLASS] and keep calling them in [CHILD CLASS]
    
    
    #user who is not register will have only get access, the user who is authenticated can get,post,put and patch..
    #We will work in ordet to get up the required throttle for the anon(anonymous) user