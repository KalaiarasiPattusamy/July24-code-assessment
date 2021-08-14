import re
def validation(name,mobilenum,emailid,pincode):
    vname=re.search("^[A-Za-z]{2,25}$",name)
    vmob=re.search("^(\+91)?[0]?(91)?[6-9]\d{9}$",mobilenum)
    vmail=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",emailid)
    vpin=re.search("^[6]\d{5}$",pincode)
    if vname and vmob and vmail and vpin:
        return True
    else:
        return False



