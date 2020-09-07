from random import randint

from django.db import models
from django.utils.translation import gettext_lazy as _


class MetaModel(models.Model):
    """Core model"""

    name = models.CharField(_('Item name'), unique=False, max_length=128, blank=False, null=False)

    def __str__(self):
        super().__str__()
        return self.name


class CountryModel(MetaModel):
    """Common Country model"""
    class Meta:
        verbose_name_plural = _("Countries")


class RegionModel(MetaModel):
    """Common region model (depends on Country)"""
    class Meta:
        verbose_name_plural = _("Regions")

    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, blank=True, null=True)


class AreaModel(MetaModel):
    """Common area model (depends on region)"""
    class Meta:
        verbose_name_plural = _("Areas")

    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, blank=True, null=True)


class MarkModel(MetaModel):
    """Common quality mark model (depends on Country, region and area)"""
    class Meta:
        verbose_name_plural = _("Quality marks")

    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, blank=True, null=True)


class SignModel(MetaModel):
    """Common "wine sign" model (depends on Country, region. area and quality mark)"""

    def __str__(self):
        super().__str__()
        return f'Sign {self.id} ({self.name})'

    class Meta:
        verbose_name_plural = _("Signs")
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, blank=True, null=True)
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE, blank=True, null=True)
    sign = models.CharField(_('Wine sign'), max_length=1, null=True)
    quality_mark = models.ForeignKey(MarkModel, on_delete=models.CASCADE, blank=True, null=True)

