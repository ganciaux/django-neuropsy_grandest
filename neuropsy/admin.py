from django.contrib import admin
from .models import Appointment, Client, Article, Order, OrderData, Payment

admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Article)
admin.site.register(Payment)

class OrderDataInline(admin.TabularInline):
    model = OrderData
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDataInline,
    ]

admin.site.register(Order, OrderAdmin)