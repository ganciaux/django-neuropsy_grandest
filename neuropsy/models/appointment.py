from django.db import models
from .client import Client
from .order import Order
from .timestamp import TimeStampedModel


class Appointment(TimeStampedModel):
    APPOINTMENT_TYPE_NONE = 'NONE'
    APPOINTMENT_TYPE_INITIAL = 'INITIAL'
    APPOINTMENT_TYPE_RESTITUTION = 'RESTITUTION'
    APPOINTMENT_TYPE_BILAN = 'BILAN'
    APPOINTMENT_TYPE_FOLLOW_UP = 'FOLLOW_UP'
    APPOINTMENT_TYPE_SYNTHESIS = 'SYNTHESIS'
    APPOINTMENT_TYPE_CHOICES = [
        (APPOINTMENT_TYPE_NONE, 'Aucun'),
        (APPOINTMENT_TYPE_INITIAL, 'Consultation initiale'),
        (APPOINTMENT_TYPE_RESTITUTION, 'Restitution'),
        (APPOINTMENT_TYPE_BILAN, 'Bilan'),
        (APPOINTMENT_TYPE_FOLLOW_UP, 'Suivi'),
        (APPOINTMENT_TYPE_SYNTHESIS, 'Synthèse'),
    ]
    type = models.CharField(
        max_length=16,
        choices=APPOINTMENT_TYPE_CHOICES,
        default=APPOINTMENT_TYPE_NONE,
    )
    APPOINTMENT_STATUS_NONE = 'NONE'
    APPOINTMENT_STATUS_COMING = 'COMING'
    APPOINTMENT_STATUS_CANCELED = 'CANCELED'
    APPOINTMENT_STATUS_FINISHED = 'FINISHED'
    APPOINTMENT_STATUS_POSTPONED = 'POSTPONED'
    APPOINTMENT_STATUS_CHOICES = [
        (APPOINTMENT_STATUS_NONE, 'Aucun'),
        (APPOINTMENT_STATUS_COMING, 'A venir'),
        (APPOINTMENT_STATUS_CANCELED, 'Annulé'),
        (APPOINTMENT_STATUS_FINISHED, 'Terminé'),
        (APPOINTMENT_STATUS_POSTPONED, 'Reporté'),
    ]
    status = models.CharField(
        max_length=16,
        choices=APPOINTMENT_STATUS_CHOICES,
        default=APPOINTMENT_STATUS_NONE,
    )
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.date.strftime("%d-%m-%Y %H:%M") + ' ' + self.client.first_name

    def get_date_display(self):
        return self.date.strftime("%d-%m-%Y %H:%M")
