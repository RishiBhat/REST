
from django.contrib import admin
from django.db import router
from django.urls import path, include
from app22 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()
router.register('fc',views.fc, basename='fc')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #path('gettoke/',views.CustomToken.as_view()),       #here we are getting the token with signals, if user is already created or not

]
