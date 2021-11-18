

from django.contrib import admin
from django.urls import path
from app36 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fc/', views.StudentView.as_view()),
    
]

