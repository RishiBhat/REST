from django.contrib import admin

# Register your models here.
from app22.models import Student

@admin.register(Student)


class StudentAdmin(admin.ModelAdmin):
    fields=['id','name','roll','city']

    