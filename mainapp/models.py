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


class Area(models.Model):
    """Common area model (depends on region)"""
    class Meta:
        verbose_name_plural = "Areas"

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField('Area name', max_length=128)

    def __str__(self):
        return self.name


class QualityMark(models.Model):
    """Common quality mark model (depends on Country, region and area)"""
    class Meta:
        verbose_name_plural = "Quality marks"

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField('Quality mark', max_length=64)

    def __str__(self):
        return self.name


class Sign(models.Model):
    """Common "wine sign" model (depends on Country, region. area and quality mark)"""
    class Meta:
        verbose_name_plural = "Signs"

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    quality_mark = models.ForeignKey(QualityMark, on_delete=models.CASCADE)
    sign = models.CharField('Wine sign', max_length=1)
    name = models.CharField('Sign', max_length=64)

    def __str__(self):
        return f'Sign {self.id} ({self.country}, {self.region})'
