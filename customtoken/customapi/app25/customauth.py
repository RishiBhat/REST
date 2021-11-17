from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuth(BaseAuthentication):                   #The Custom authentication should subclass the BaseAuthentication
    def authenticate(self, request):
#-----------------------[Logic Comes here to get succeded in a way], after this logic we shall return the user and auth otherwise None...... '
        
        username = request.GET.get('username')
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)     #This is the username which we fetch from the db
        
        except User.DoesNotExist:
            raise AuthenticationFailed('No such User')

        return (user, None)



