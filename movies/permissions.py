from rest_framework.permissions import IsAdminUser, BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_employee)