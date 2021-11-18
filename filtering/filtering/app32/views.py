from django.shortcuts import render
from rest_framework import authentication, permissions

# Create your views here.
from app32.models import Student
from app32.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication


class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
#    authentication_classes = [SessionAuthentication]
#To perform the filter in data we will just override .getQueryset

    def get_queryset(self):
        user = self.request.user           #this gives us the current user
        return Student.objects.filter(invigilator=user) #This is the current user data, logged in user filter data
        

    