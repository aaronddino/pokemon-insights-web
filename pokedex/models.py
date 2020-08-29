from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Pokemon')
    typeOne = models.CharField(max_length=255, null=False, blank=False, verbose_name='Type (One)')
    typeTwo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Type (Two)')
    weight = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False, verbose_name='Weight')
    height = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False, verbose_name='Height')