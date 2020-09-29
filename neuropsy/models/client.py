from django.db import models
from django.db.models import ForeignKey

from .timestamp import TimeStampedModel


class Client(TimeStampedModel):
    CLIENT_TYPE_NONE = 'NONE'
    CLIENT_TYPE_MISS = 'MISS'
    CLIENT_TYPE_MRS = 'MRS'
    CLIENT_TYPE_MR = 'MR'
    CLIENT_TYPE_COMPANY = 'COMPANY'
    CLIENT_TYPE_CHOICES = [
        (CLIENT_TYPE_NONE, 'Aucun'),
        (CLIENT_TYPE_MISS, 'Mademoiselle'),
        (CLIENT_TYPE_MRS, 'Madame'),
        (CLIENT_TYPE_MR, 'Monsieur'),
        (CLIENT_TYPE_COMPANY, 'Société'),
    ]
    type = models.CharField(
        verbose_name='Type',
        max_length=16,
        choices=CLIENT_TYPE_CHOICES,
        default=CLIENT_TYPE_NONE,
    )
    CLIENT_COUNTRY_NONE = 'NONE'
    CLIENT_COUNTRY_OTHER = 'OTHER'
    CLIENT_COUNTRY_FR = 'FR'
    CLIENT_COUNTRY_LUX = 'LU'
    CLIENT_COUNTRY_DE = 'DE'
    CLIENT_COUNTRY_BE = 'BE'
    CLIENT_COUNTRY_CHOICES = [
        (CLIENT_COUNTRY_NONE, 'Aucun'),
        (CLIENT_COUNTRY_OTHER, 'Autre'),
        (CLIENT_COUNTRY_FR, 'France'),
        (CLIENT_COUNTRY_LUX, 'Luxembourg'),
        (CLIENT_COUNTRY_DE, 'Allemagne'),
        (CLIENT_COUNTRY_BE, 'Belgique'),
    ]
    country = models.CharField(
        verbose_name='Pays',
        max_length=8,
        choices=CLIENT_COUNTRY_CHOICES,
        default=CLIENT_COUNTRY_FR,
    )
    CLIENT_STATUS_OK = 'OK'
    CLIENT_STATUS_BLOCKED = 'BLOCKED'
    CLIENT_STATUS_CONTENTIOUS = 'CONTENTIOUS'
    CLIENT_STATUS_RECOVERY = 'RECOVERY'
    CLIENT_STATUS_UNDESIRED = 'UNDESIRED'
    CLIENT_STATUS_CHOICES = [
        (CLIENT_STATUS_OK, 'Ok'),
        (CLIENT_STATUS_BLOCKED, 'Bloqué'),
        (CLIENT_STATUS_CONTENTIOUS, 'Contentieux'),
        (CLIENT_STATUS_RECOVERY, 'Recouvrement'),
        (CLIENT_STATUS_UNDESIRED, 'Non désiré'),
    ]
    status = models.CharField(
        verbose_name='Statut',
        max_length=16,
        choices=CLIENT_STATUS_CHOICES,
        default=CLIENT_STATUS_OK,
    )
    first_name = models.CharField(max_length=64, verbose_name='Prénom')
    last_name = models.CharField(max_length=64, verbose_name='Nom')
    email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=32, blank=True, verbose_name='Téléphone')
    address = models.CharField(max_length=32, blank=True, verbose_name='Adresse')
    city = models.CharField(max_length=32, blank=True, verbose_name='Ville')
    zip = models.CharField(max_length=32, blank=True, verbose_name='Code postal')
    CLIENT_ORIGIN_NONE = 'NONE'
    CLIENT_ORIGIN_INTERNET = 'INTERNET'
    CLIENT_ORIGIN_CAMPS = 'CAMPS'
    CLIENT_ORIGIN_LIBERAL = 'LIBERAL'
    CLIENT_ORIGIN_PMI = 'PMI'
    CLIENT_ORIGIN_CHOICES = [
        (CLIENT_ORIGIN_NONE, 'Aucun'),
        (CLIENT_ORIGIN_INTERNET, 'Internet'),
        (CLIENT_ORIGIN_CAMPS, 'CAMPS'),
        (CLIENT_ORIGIN_LIBERAL, 'Libéral'),
        (CLIENT_ORIGIN_PMI, 'PMI')
    ]
    origin = models.CharField(
        verbose_name = 'Origine',
        max_length=16,
        choices=CLIENT_ORIGIN_CHOICES,
        default=CLIENT_ORIGIN_NONE,
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name='Date de naissance')
    description = models.TextField(blank=True, verbose_name='Description')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_label(self):
        return self.first_name + ' ' + self.last_name

