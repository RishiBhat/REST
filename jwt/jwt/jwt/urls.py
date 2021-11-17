
from django.contrib import admin
from django.urls import path, include
from app28 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token                   #to get the user verified and get api token we just import a view
from rest_framework_simple_jwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router =DefaultRouter()
router.register('fc',views.fc, basename='fc')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(router.urls)),
   # path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('refreshtoken/',TokenRefreshView.as_view(), name='token_obtain_pair'),
   # path('verifytoken/', TokenVerifyView.as_view(), name='token_obtain_pair'),
    #path('auth/',include('rest_framework.urls', namespace='rest_framework')), #This is for the browsable api
    #path('gettoken/',CustomAuthToken.as_view()), #this is the api endpoint exposed  #if  user sends requests in gettoken it will forward a custom token.....

]