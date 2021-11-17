
from posixpath import basename
from django.contrib import admin
from django.urls import path, include   
from app18 import views
from rest_framework.routers import DefaultRouter


#creating Router object
router = DefaultRouter()

#now we wil register the viewset with router
#router.register('hi',views.StudentViewSet, basename='student')


#for now we have to tell the url where is router located
urlpatterns = [

    path('admin/',admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),

]