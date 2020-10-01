from django.contrib import admin
from .models import Appointment, Client, Article, Order, Payment

admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Article)
admin.site.register(Payment)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
