from rest_framework import serializers
from donar.models import Donar

class DonarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donar
        fields=('id','name','address','bloodgroup','mobnum','username','password')


