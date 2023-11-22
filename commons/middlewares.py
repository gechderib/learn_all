# yourapp/middlewares.py

from django.http import HttpResponse

def isRoleExist(request):
    ROLES = ["admin","renter","owner"]
    print("sdklfj" in ROLES)
    # print(len(request.data.get("roles")))
    if request.data and request.data.get("roles") is not None and (len(request.data.get("roles"))) > 0:
        for value in request.data.get("roles"):
            if value not in ROLES:
                print("not in roles")
                break
                # return False
    if request.data and (request.data.get("roles") == None or len(request.data.get("roles")) == 0):
        request.data.update({"roles":["renter"]})
        return True
