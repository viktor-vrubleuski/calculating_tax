from django.db import models


class TaxBand(models.Model):
    earnings_up_to = models.IntegerField(blank=True, null=True)
    percent = models.SmallIntegerField()

    class Meta:
        db_table = 'tax_band'
        verbose_name = 'tax band'
