from django.db import models
from .client import Client
from .order import Order
from .timestamp import TimeStampedModel


class Payment(TimeStampedModel):

    PAYMENT_TYPE_NONE = 'NONE'
    PAYMENT_TYPE_CHECK = 'CHECK'
    PAYMENT_TYPE_CASH = 'CASH'
    PAYMENT_TYPE_CREDIT_CARD = 'CREDIT_CARD'
    PAYMENT_TYPE_TRANSFER = 'TRANSFER'
    PAYMENT_TYPE_OTHER = 'OTHER'
    PAYMENT_TYPE_CHOICES = [
        (PAYMENT_TYPE_NONE, 'Aucun'),
        (PAYMENT_TYPE_CHECK, 'Chèque'),
        (PAYMENT_TYPE_CASH, 'Espèce'),
        (PAYMENT_TYPE_CREDIT_CARD, 'Carte de crédit'),
        (PAYMENT_TYPE_TRANSFER, 'Virement'),
        (PAYMENT_TYPE_OTHER, 'Autre'),
    ]
    type = models.CharField(
        max_length=16,
        choices=PAYMENT_TYPE_CHOICES,
        default=PAYMENT_TYPE_NONE,
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Montant')
    date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.date.strftime("%d-%m-%Y %H:%M") + ' ' + self.client.first_name + '(' + str(self.price) + ')'

    def get_date_display(self):
        return self.date.strftime("%d-%m-%Y %H:%M")
