from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from app24.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
     list_display = ['id','name','roll','city']
