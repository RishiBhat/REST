

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app14 import views


router = DefaultRouter()

router.register('hi',views.StudentModelViewSet, basename='student')
#router.register('hi',views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))                    #this is for the login credential carried over the page
]
