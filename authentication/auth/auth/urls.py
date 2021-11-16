

from django.contrib import admin
from django.urls import path, include   
from rest_framework.routers import DefaultRouter
from app12 import views


router = DefaultRouter()

router.register('hi',views.StudentModelViewSet, basename='student')
#router.register('hi',views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
