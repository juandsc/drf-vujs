from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        safe_method = request.method in permissions.SAFE_METHODS
        return safe_method or is_admin