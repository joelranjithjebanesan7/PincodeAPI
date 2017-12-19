from rest_framework import serializers
from pincodes.models import Pincode
from rest_framework import pagination
from django.core.paginator import PageNotAnInteger,EmptyPage
 
 
class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pincode
        fields = ('id', 'officename', 'pincode', 'officetype', 'Deliverystatus', 'regionname', 'circlename','taluk')




    