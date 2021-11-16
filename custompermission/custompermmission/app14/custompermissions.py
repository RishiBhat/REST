from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True   
        return False

#if the other files and logic can be build here