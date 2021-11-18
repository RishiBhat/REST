from rest_framework.routers import DefaultRouter
from app31 import views
from django.contrib import admin
from django.urls import path, include


#router = DefaultRouter()
#router.register('fc',views.fc, basename='fc')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fc',views.StudentList.as_view()),
    #path('fc',views.StudentCreate.as_view()),
    #path('fc/<int:pk>',views.StudentUpdate.as_view()),
    #path('fc/<int:pk>',views.StudentDestroy.as_view()),
]
