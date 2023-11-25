from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("admin" in request.user.roles)


class IsRenter(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("renter" in request.user.roles)


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("owner" in request.user.roles)
