from django.db import models


class Country(models.Model):
    """Common Country model"""
    class Meta:
        verbose_name_plural = "Countries"

    name = models.CharField('Country name', unique=True,  max_length=128)

    def __str__(self):
        return self.name


class Region(models.Model):
    """Common region model (depends on Country)"""
    class Meta:
        verbose_name_plural = "Regions"

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField('Region name', max_length=128)

    def __str__(self):
        return self.name


class Sign(models.Model):
    """Common "wine sign" model (depends on Country, region. area and quality mark)"""
    class Meta:
        verbose_name_plural = "Signs"

    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('Sign', max_length=60, blank=True, null=True)

    def __str__(self):
        return f'Sign {self.id} ({self.country}, {self.region})'
