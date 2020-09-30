from django.contrib import admin
from .models import Appointment, Client, Article, Order

admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Article)
admin.site.register(Order)
