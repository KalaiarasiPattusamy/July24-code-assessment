from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from donar.serializers import DonarSerializer
from donar.models import Donar
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests




def addata(request):
    return render(request,"index.html")

def viewall(request):
    fetchdata=requests.get("http://127.0.0.1:8000/donar/viewall/").json()
    return render(request,"viewdonar.html",{"data":fetchdata})

def updation(request):
    return render(request,"updatedonar.html")








@csrf_exempt
def adddonar(request):
    if(request.method=="POST"):
        
        # mydict=JSONParser().parse(request)
        donar_serialize=DonarSerializer(data=request.POST)
        if (donar_serialize.is_valid()):
            donar_serialize.save()
            return redirect(viewall)
            return JsonResponse(donar_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def donar_list(request):
    if(request.method=="GET"):
        donars=Donar.objects.all()
        donar_serializer=DonarSerializer(donars,many=True)
        return JsonResponse(donar_serializer.data,safe=False)



@csrf_exempt
def updatesearchapi(request):
    try:
        getmob=request.POST.get("mobnum")
        getdonar=Donar.objects.filter(mobnum=getmob)
        donar_serializer=DonarSerializer(getdonar,many=True)
        return render(request,"updatedonar.html",{"data":donar_serializer.data})
        return JsonResponse(donar_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Donar.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def updatedataread(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewadd=request.POST.get("newadd")
    getnewblood=request.POST.get("newblood")
    getnewmob=request.POST.get("newmob")
    getnewuser=request.POST.get("newuser")
    getnewpass=request.POST.get("newpass")

    mydata={'id':getnewid,'name':getnewname,'address':getnewadd,'bloodgroup':getnewblood,'mobnum':getnewmob,'username':getnewuser,'password':getnewpass}
    jsondata=json.dumps(mydata)
    apilink="http://127.0.0.1:8000/donar/viewone/" + getnewid
    requests.put(apilink,data=jsondata)
    return HttpResponse("data updated successfully")

@csrf_exempt
def donar_details(request, id):
    try:
        donars=Donar.objects.get(id=id)
    except Donar.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        donar_serializer=DonarSerializer(donars)
        return JsonResponse(donar_serializer.data,safe=False,status=status.HTTP_200_OK)  
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        donar_serialize=DonarSerializer(donars,data=mydict)
        if (donar_serialize.is_valid()):
            donar_serialize.save()
            return JsonResponse(donar_serialize.data,status=status.HTTP_200_OK)
        

def loginn(request):
    return render(request,"login.html")

def welcomee(request):
    return render(request,"welcome.html")



@csrf_exempt
def login_check(request):

    try:
        username=request.POST.get("username")
        password=request.POST.get("password")

        getdonar=Donar.objects.filter(username=username,password=password)
        donar_serializer=DonarSerializer(getdonar,many=True)
        if(donar_serializer.data):
            for i in donar_serializer.data:
                x=i["name"]
                y=i["id"]
                print(x)
            request.session['uname']=x
            request.session['uid']=y
            return render(request, "updatedonar.html")
        else:
            return HttpResponse("Invalid credentials")
    
    except:
        return HttpResponse("something went wrong")

