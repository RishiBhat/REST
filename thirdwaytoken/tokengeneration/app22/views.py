from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from  app22.models import Student
from app22.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class fc(viewsets.ModelViewSet):
    pass