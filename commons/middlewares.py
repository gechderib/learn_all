import json


def isRoleExist(request):
    ROLES = ["admin","renter","owner"]
    result = True
    print(request.data)
    if request.data and request.data.get("roles") is not None and (len(request.data.get("roles"))) > 0:
        roles = json.loads(request.data.get("roles"))
        for value in roles:
            if value not in ROLES:
                result = False
                break        
    return result

def isAdminRoleExist(request):
    if request.data and request.data.get("roles") is not None:
        roles = json.loads(request.data.get("roles"))
        if "admin" in roles:
            return True
    return False

def isOtherRoleExist(request):
    if ("renter" in  roles) or ("owner" in roles):
        return True

