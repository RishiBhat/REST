from django.contrib import admin
from main.models import Emp
# Register your models here.


@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone']

