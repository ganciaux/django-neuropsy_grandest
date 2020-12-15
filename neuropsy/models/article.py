from django.db import models
from django.db.models import ForeignKey

from .timestamp import TimeStampedModel


class Article(TimeStampedModel):
    label = models.CharField(max_length=64, verbose_name='Label')
    amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix')
    reference = models.CharField(max_length=64, default="", verbose_name='Réference')
    description = models.TextField(blank=True, verbose_name='Description')

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return self.label + ' ' + str(self.amount)

    def get_label(self):
        return self.label + ' ' + str(self.amount)

