from django.contrib import admin
from .models import Appointment, Client, Article, Order, OrderData, Payment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_filter = ['origin']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ['date', 'type', 'client']


admin.site.register(Article)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ['date', 'type', 'client']


class OrderDataInline(admin.TabularInline):
    model = Order.articles.through
    extra = 1
    verbose_name = "ligne de commande"


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDataInline]


@admin.register(Order)
class OrderAdmin(OrderAdmin):
    list_filter = ['date', 'status', 'client']
