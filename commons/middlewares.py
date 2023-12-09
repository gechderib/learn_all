

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

def isImageExist(request):
    images = request.FILES.getlist('images')
    if(len(images) < 2):
        return False
    return True

def isAddingImage(request):
    if request.data.get("is_adding_image") is not None:
        return True
    return False

