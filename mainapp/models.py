from django.db import models
from django.utils.translation import gettext_lazy as _


class MetaModel(models.Model):
    """Core model"""
    name = models.CharField(_('MODEL NAME METHOD'), unique=False, max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name or None


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

    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE)


class MarkModel(MetaModel):
    """Common quality mark model (depends on Country, region and area)"""
    class Meta:
        verbose_name_plural = _("Quality marks")

    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)


class SignModel(MetaModel):
    """Common "wine sign" model (depends on Country, region. area and quality mark)"""
    class Meta:
        verbose_name_plural = _("Signs")

    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE)
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    sign = models.CharField(_('Wine sign'), max_length=1, null=True)
    quality_mark = models.ForeignKey(MarkModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Sign {self.id} ({self.name})'
