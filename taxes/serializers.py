from rest_framework import serializers


class EarningsSerializer(serializers.Serializer):
    income = serializers.IntegerField(style={'placeholder': 'Please, input your earnings'})
    detail = serializers.BooleanField()

    class Meta:
        fields = ('income',)


class TaxSerializer(serializers.Serializer):
    income = serializers.IntegerField(min_value=0, max_value=1000000000000000000)
    detail = serializers.BooleanField()

    class Meta:
        fields = ('income',)

    def __init__(self, first_band, second_band, third_band, fourth_band, *args, **kwargs):
        self._first_band = first_band
        self._second_band = second_band
        self._third_band = third_band
        self._fourth_band = fourth_band
        super().__init__(*args, **kwargs)

    def income_tax_band_1(self, income):
        if income <= self._first_band.earnings_up_to:
            return 0
        if income > self._second_band.earnings_up_to:
            income = self._second_band.earnings_up_to
        income -= self._first_band.earnings_up_to
        return income * (self._second_band.percent / 100)

    def income_tax_band_2(self, income):
        if income <= self._second_band.earnings_up_to:
            return 0
        if income > self._third_band.earnings_up_to:
            income = self._third_band.earnings_up_to
        income -= self._second_band.earnings_up_to
        return income * (self._third_band.percent / 100)

    def income_tax_band_3(self, income):
        if income <= self._third_band.earnings_up_to:
            return 0
        income -= self._third_band.earnings_up_to
        return income * (self._fourth_band.percent / 100)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        income = data['income']
        if income <= self._first_band.earnings_up_to:
            return dict(tax_result=0, detail=data['detail'])
        income_tax_band_1 = self.income_tax_band_1(income)
        income_tax_band_2 = self.income_tax_band_2(income)
        income_tax_band_3 = self.income_tax_band_3(income)
        if data['detail']:
            return dict(
                tax_result=income_tax_band_1 + income_tax_band_2 + income_tax_band_3,
                income_tax_slab_1=income_tax_band_1,
                income_tax_slab_2=income_tax_band_2,
                income_tax_slab_3=income_tax_band_3,
                detail=data['detail']
            )
        return dict(tax_result=income_tax_band_1 + income_tax_band_2 + income_tax_band_3, detail=data['detail'])
