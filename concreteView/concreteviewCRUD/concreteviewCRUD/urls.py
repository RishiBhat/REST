"""concreteviewCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app7 import views

urlpatterns = [

    path('admin/',admin.site.urls),
    #path('hi/', views.StudentList.as_view()),                        #shows us the list view
    #path('hi/<int:pk>/',views.StudentRetrieve.as_view()),              #shows us the POST form
    #path('hi/<int:pk>/',views.StudentUpdate.as_view()),              
    #path('hi/<int:pk>/',views.StudentDelete.as_view()),              
    #path('hi/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),              
    path('hi/<int:pk>/',views.StudentupdateDestroyRetrieve.as_view()),              
    path('hi/', views.StudentRetrieveUpdate.as_view()),          #give us the list and create option
]
