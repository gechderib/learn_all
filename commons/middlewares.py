
def isRoleExist(request):
    ROLES = ["admin","renter","owner"]
    result = True

    if request.data and request.data.get("roles") is not None and (len(request.data.get("roles"))) > 0:
        for value in request.data.get("roles"):
            print(value)
            if value not in ROLES:
                result = False
                break        
    return result

def isAdminRoleExist(request):
    if request.data and "admin" in request.data.get("roles"):
        return True
    return False

def isOtherRoleExist(request):
    if ("renter" in  request.data.get("roles")) or ("owner" in request.data.get("roles")):
        return True
