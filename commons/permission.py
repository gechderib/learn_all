from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("admin" == request.user.role)


class IsRenter(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("renter" == request.user.role)


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("owner" == request.user.role)
