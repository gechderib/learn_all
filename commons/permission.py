from rest_framework.permissions import BasePermission

class IsRoleExist(BasePermission):
    def has_permission(self, request, view):
        ROLES = ["admin","renter","owner"]
        if request.user and len(request.user.roles) > 0:
            for i in range (len(request.user.roles)):
                if request.user.roles[i] not in ROLES:
                    return False
            return True
        if request.user and len(request.user.roles) == 0:
            request.user.roles[0] = "renter"
            return True
        return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("admin" in request.user.roles)



class IsRenter(BasePermission):
    def has_permission(self, request, view):
        return request.user and ("renter" in request.user.roles)


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return 