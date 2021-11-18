from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from app34.models import Student
from app34.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter


class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
  


