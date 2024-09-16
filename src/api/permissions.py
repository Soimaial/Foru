from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

class PreventPutAndDelete(permissions.BasePermission):
    """
    Permission pour bloquer les requêtes PUT et DELETE.
    """
    def has_permission(self, request, view):
        if request.method in ['PUT', 'DELETE']:
            # Lever une exception indiquant que ces méthodes ne sont pas autorisées
            raise MethodNotAllowed(request.method, detail="cette action n'est pas permise.")
        return True
