from rest_framework.permissions import IsAdminUser, BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_employee)    

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user != obj:
            return request.user.is_employee
        elif request.user.is_authenticated and request.user == obj:
            return True