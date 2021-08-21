from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from rest_framework.parsers import JSONParser
from patient.serializers import PatientSerializer
from patient.models import Patient
from rest_framework import status
# Create your views here.





@csrf_exempt
def addpatient(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        patient_serialize=PatientSerializer(data=mydict)
        if (patient_serialize.is_valid()):
            patient_serialize.save()
            return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def viewall_patient(request):
    if(request.method=="GET"):
        patients=Patient.objects.all()
        patient_serializer=PatientSerializer(patients,many=True)
        return JsonResponse(patient_serializer.data,safe=False)
        
@csrf_exempt
def patient_details(request, patient_code):
    try:
        patients=Patient.objects.get(patient_code=patient_code)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        patient_serializer=PatientSerializer(patients)
        return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        patients.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        patient_serialize=PatientSerializer(patients,data=mydict)
        if (patient_serialize.is_valid()):
            patient_serialize.save()
            return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)
        
def addpage(request):
    return render(request,"index.html")
