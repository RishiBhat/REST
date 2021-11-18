
from django.contrib import admin
from django.db import router
from django.urls import path, include
from app30 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()
router.register('fc',views.fc, basename='fc')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth',include('rest_framework.urls',namespace='rest_framework')), #This is for the browsable api view path...
    #path('rest_framework', )

]
