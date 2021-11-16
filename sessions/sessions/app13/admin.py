from django.contrib import admin

# Register your models here.


from app13.models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll', 'city']

