from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def addstudent(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getadmin=request.POST.get("adminno")
        getrollno=request.POST.get("rollno")
        getcollege=request.POST.get("college")
        getparentname=request.POST.get("parentname")
        dict={"name":getName,"adminno":getadmin,"rollno":getrollno,"college":getcollege,"parentname":getparentname}
        result=json.dumps(dict)
        return HttpResponse(result)
    else:
        return HttpResponse("no get mathod allowed")

