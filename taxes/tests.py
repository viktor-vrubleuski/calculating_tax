from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from taxes.models import TaxBand


class AccountTests(APITestCase):

    def test_calculate_valid_value(self):
        url = reverse('calculate_tax')
        data = {'income': 52000, 'detail': False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['data']['tax_result'], 8300)
        self.assertEqual(response.data['data']['detail'], False)
        self.assertEqual(len(response.data['data']), 2)

    def test_calculate_valid_value_with_detail(self):
        url = reverse('calculate_tax')
        data = {'income': 52000, 'detail': True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data['data']['tax_result'], 8300)
        self.assertEqual(response.data['data']['income_tax_slab_1'], 7500)
        self.assertEqual(response.data['data']['income_tax_slab_2'], 800)
        self.assertEqual(response.data['data']['income_tax_slab_3'], 0)
        self.assertEqual(response.data['data']['detail'], True)
        self.assertEqual(len(response.data['data']), 5)

    def test_calculate_invalid_value(self):
        url = reverse('calculate_tax')
        data = {'income': '5200t0', 'detail': False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data), 1)

    def test_calculate_invalid_value_with_detail(self):
        url = reverse('calculate_tax')
        data = {'income': '5200t0', 'detail': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response.data), 1)

    def test_send_not_allowed_method_get(self):
        url = reverse('calculate_tax')
        data = {'income': '5200t0', 'detail': True}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_send_not_allowed_method_put(self):
        url = reverse('calculate_tax')
        data = {'income': '5200t0', 'detail': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_send_not_allowed_method_delete(self):
        url = reverse('calculate_tax')
        data = {'income': '5200t0', 'detail': True}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_exists_tax_bands(self):
        self.assertEqual(TaxBand.objects.count(), 4)
        self.assertEqual(TaxBand.objects.get(id=1).percent, 0)
        self.assertEqual(TaxBand.objects.get(id=2).percent, 20)
        self.assertEqual(TaxBand.objects.get(id=3).percent, 40)
        self.assertEqual(TaxBand.objects.get(id=4).percent, 45)
