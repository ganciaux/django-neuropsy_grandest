from django.db import models
from .client import Client
from .article import Article
from .timestamp import TimeStampedModel


class Order(TimeStampedModel):
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
    )
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article, through='OrderData')

    def __str__(self):
        return self.date.strftime("%d-%m-%Y %H:%M") + ' ' + self.client.first_name

    def get_date_display(self):
        return self.date.strftime("%d-%m-%Y %H:%M")

    def get_total(self):
        total = 0.00
        for data in OrderData.objects.filter(order_id=self.id):
            total += data.quantity * data.article.amount
        return total;


class OrderData(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
