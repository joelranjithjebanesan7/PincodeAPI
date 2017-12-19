from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pincodes.models import Pincode
from pincodes.views import PincodeList,PincodeDetail
from pincodes.serializers import PincodeSerializer
 


class PincodeTest(APITestCase):
    def test_pincode_lists(self):
        url = reverse('pincode-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(Pincode.objects.all())