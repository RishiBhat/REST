from django.shortcuts import render
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import authentication_classes, permission_classes

# Create your views here.
from app20.models import Student
from app20.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class fc(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_classes = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]