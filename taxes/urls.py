from django.urls import path

from taxes.views import MainView, TaxView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('api/calculate-tax/', TaxView.as_view(), name='calculate_tax'),
]
