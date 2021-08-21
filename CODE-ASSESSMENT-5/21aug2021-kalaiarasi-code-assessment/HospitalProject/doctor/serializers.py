from rest_framework import serializers
from doctor.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('doctor_code','name','address','speciality','username','password')

