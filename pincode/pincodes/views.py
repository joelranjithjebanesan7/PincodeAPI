from django.contrib.auth.models import User
from pincodes.serializers import PincodeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from pincodes.models import Pincode
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

class PincodeList(generics.ListAPIView):
    queryset = Pincode.objects.all()
    serializer_class = PincodeSerializer
    paginaion_class = PageNumberPagination

class PincodeDetail(generics.ListAPIView):
    serializer_class = PincodeSerializer
    model = serializer_class.Meta.model
    def get_queryset(self):
        pincode = self.kwargs['pincode']
        queryset = self.model.objects.filter(pincode=pincode)
        return queryset
 
 