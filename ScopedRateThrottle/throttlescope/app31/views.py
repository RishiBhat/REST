from django.shortcuts import render
from rest_framework import authentication

# Create your views here.
from app31.models import Student
from app31.serializers import StudentSerializer
from rest_framework import viewsets, serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

#ScopedRateThrottle can be performed on the various individual parts...
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_class  = [ScopedRateThrottle]
    throttle_scope ='ViewStu'                    #This is the data which we get from the ViewStu in scope  
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class  = [ScopedRateThrottle]
    throttle_scope = 'modifystu'
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class  = [ScopedRateThrottle]
    throttle_scope = 'modifystu'
class Retrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer
    throttle_class  = [ScopedRateThrottle]
    throttle_class = 'ViewStu'                    #This only reflects the data of single object

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_class  = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

