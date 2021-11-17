from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.


from app28.models import Student
from app28.serializers import StudentSerializer

class fc(viewsets.ModelViewSet):
    pass
