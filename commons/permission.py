from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print("jjjjjjjjj")
        return request.user and request.user.role == "admin"

class IsTech(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == "tech"