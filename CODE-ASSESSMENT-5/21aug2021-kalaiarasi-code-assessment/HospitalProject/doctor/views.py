from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from rest_framework.parsers import JSONParser
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor
from rest_framework import status
# Create your views here.





@csrf_exempt
def adddoctor(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        doctor_serialize=DoctorSerializer(data=mydict)
        if (doctor_serialize.is_valid()):
            doctor_serialize.save()
            return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def viewall_doctor(request):
    if(request.method=="GET"):
        doctors=Doctor.objects.all()
        doctor_serializer=DoctorSerializer(doctors,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)
        
@csrf_exempt
def doctor_details(request, doctor_code):
    try:
        doctors=Doctor.objects.get(doctor_code=doctor_code)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        doctor_serializer=DoctorSerializer(doctors)
        return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        doctors.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        doctor_serialize=DoctorSerializer(doctors,data=mydict)
        if (doctor_serialize.is_valid()):
            doctor_serialize.save()
            return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)
        
def registerpage(request):
    return render(request,"indexd.html")


def loginpage(request):
    return render(request,"indexl.html")
