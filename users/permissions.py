from rest_framework.permissions import IsAdminUser, BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_employee)
    
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_employee)