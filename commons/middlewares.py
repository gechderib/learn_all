

def isRoleExist(request):
    ROLES = ["admin","renter","owner"]
    if request.data and (request.data.get("role") in ROLES or request.data.get("role") is None):
        return True
    return False

def isAdminRoleExist(request):
    if request.data and request.data.get("role") == "admin":
        return True
    return False

def isOtherRoleExist(request):
    ROLES = ["admin","renter","owner"]
    if request.data and request.data.get("role") not in ROLES:
        return True
    return False
