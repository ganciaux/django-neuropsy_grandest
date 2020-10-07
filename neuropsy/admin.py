from django.contrib import admin
from .models import Appointment, Client, Article, Order, OrderData, Payment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']


admin.site.register(Appointment)
admin.site.register(Article)
admin.site.register(Payment)


class OrderDataInline(admin.TabularInline):
    model = Order.articles.through
    extra = 1
    verbose_name = "ligne de commande"


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDataInline,
    ]


admin.site.register(Order, OrderAdmin)
