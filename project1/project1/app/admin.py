from django.contrib import admin

# Register your models here.
from .models import Portfolio





@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=['id','name','state','msg']


