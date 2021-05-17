from django.core.cache import cache
from rest_framework import status

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from taxes.constants import TAX_BAND_UP_TO_12500, TAX_BAND_UP_TO_50000, TAX_BAND_UP_TO_150000, TAX_BAND_OVER_150000
from taxes.models import TaxBand
from taxes.serializers import EarningsSerializer, TaxSerializer, TaxInternalSerializer


class MainView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'calculating_tax.html'

    def get(self, request):
        serializer = EarningsSerializer()
        return Response({'serializer': serializer})


class TaxView(APIView):

    @staticmethod
    def get_data(tax_band_id):
        if not cache.get(tax_band_id):
            cache.set(tax_band_id, TaxBand.objects.get(id=tax_band_id))
        return cache.get(tax_band_id)

    def post(self, request):
        first_band = self.get_data(TAX_BAND_UP_TO_12500)
        second_band = self.get_data(TAX_BAND_UP_TO_50000)
        third_band = self.get_data(TAX_BAND_UP_TO_150000)
        fourth_band = self.get_data(TAX_BAND_OVER_150000)
        if request.content_type == 'application/json':
            serializer = TaxInternalSerializer
        else:
            serializer = TaxSerializer
        serializer = serializer(
            data=request.data,
            first_band=first_band,
            second_band=second_band,
            third_band=third_band,
            fourth_band=fourth_band
        )
        if not serializer.is_valid():
            return Response(data={'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'data': serializer.data}, status=status.HTTP_200_OK)
