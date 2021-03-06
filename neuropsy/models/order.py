from django.db import models
from .client import Client
from .article import Article
from .timestamp import TimeStampedModel


class Order(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client')
    date = models.DateField(verbose_name='Date')
    reference = models.CharField(max_length=64, default="", verbose_name='Réference')
    ORDER_STATUS_IN_PROGRESS = 'IN_PROGRESS'
    ORDER_STATUS_CANCELED = 'CANCELED'
    ORDER_STATUS_FINISHED = 'FINISHED'
    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_IN_PROGRESS, 'En cours'),
        (ORDER_STATUS_CANCELED, 'Annulé'),
        (ORDER_STATUS_FINISHED, 'Terminé'),
    ]
    status = models.CharField(
        max_length=16,
        choices=ORDER_STATUS_CHOICES,
        default=ORDER_STATUS_IN_PROGRESS,
        verbose_name='Statut'
    )
    description = models.TextField(blank=True)
    articles = models.ManyToManyField(Article, through='OrderData')

    class Meta:
        verbose_name = "Commande"

    def __str__(self):
        return self.date.strftime("%d-%m-%Y %H:%M") + ' ' + self.client.first_name

    def get_date_display(self):
        return self.date.strftime("%d-%m-%Y %H:%M")

    def get_total(self):
        total = float(0.00)
        for data in OrderData.objects.filter(order_id=self.id):
            total += float(data.quantity) * float(data.article.amount)
        return total


class OrderData(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article')
    quantity = models.PositiveIntegerField(verbose_name='Quantité')
    description = models.TextField(blank=True, verbose_name='Description')

    class Meta:
        verbose_name = "Détail"
