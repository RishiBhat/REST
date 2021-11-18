from typing import List
from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from app37.models import Student
from app37.serializers import StudentSerializer
from rest_framework.generics import ListAPIView

from pagination.pagess.app37.paginations import MyPageNumberPagination

class fc(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination

    
