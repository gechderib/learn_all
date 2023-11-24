from rest_framework.permissions import BasePermission
from rest_framework.decorators import api_view, permission_classes
from commons.middlewares import isAdminRoleExist
from rest_framework.permissions import IsAuthenticated


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("admin" in request.user.roles)



class IsRenter(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("renter" in request.user.roles)


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("owner" in request.user.roles)
