from django.contrib import admin

# Register your models here.


from app3.models import Student

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city', 'roll']