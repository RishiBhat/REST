from posixpath import basename
from django.contrib import admin
from django.urls import path, include   
from app10 import views
from rest_framework.routers import DefaultRouter


#creating Router object
router = DefaultRouter()

#now we wil register the viewset with router
router.register('hi',views.StudentModelViewSet, basename='student')


#for now we have to tell the url where is router located
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
]

