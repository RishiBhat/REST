from app40 import views
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter


router = DefaultRouter
router.register('teacher', views.Teacher,'teacher')
router.register('student', views.student,'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
]
