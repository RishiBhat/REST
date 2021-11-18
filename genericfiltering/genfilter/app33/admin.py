from django.contrib import admin
from rest_framework import serializers
from rest_framework.exceptions import server_error



# Register your models here.
from app33.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll','city']

