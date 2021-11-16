from django.contrib import admin

# Register your models here.
from .models import Rishi



@admin.register(Rishi)
class RishiAdmin(admin.ModelAdmin):
    list_display=['id','employee_id','job_title','company']

