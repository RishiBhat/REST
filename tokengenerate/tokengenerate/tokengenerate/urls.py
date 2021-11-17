

from django.contrib import admin
from django.urls import path, include
from app21 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token                   #to get the user verified and get api token we just import a view
from app21.customtoken import CustomAuthToken 

router =DefaultRouter()

router.register('fc',views.fc, basename='fc')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    #path('gettoken/',CustomAuthToken.as_view()), #this is the api endpoint exposed  #if  user sends requests in gettoken it will forward a custom token..

]

