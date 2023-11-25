
def isRoleExist(request):
    ROLES = ["admin","renter","owner"]
    result = True
    if request.data and request.data.get("roles") is not None and (len(request.data.get("roles"))) > 0:
        for value in request.data.get("roles"):
            if value not in ROLES:
                result = False
                break
    if request.data and (request.data.get("roles") is None or len(request.data.get("roles")) == 0):
        request.data.update({"roles":["renter"]})
        result = True
    print(result)
    return result

def isAdminRoleExist(request):
    if "admin" in request.data.get("roles"):
        return True

def isOtherRoleExist(request):
    if ("renter" in  request.data.get("roles")) or ("owner" in request.data.get("roles")):
        return True
