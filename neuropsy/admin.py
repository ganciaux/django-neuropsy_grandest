from django.contrib import admin
from .models import Appointment, Client, Article, Order, OrderData, Payment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'client_address')
    list_filter = ['first_name']
    search_fields = ['first_name']

    def client_address(self, obj):
        address = ""
        if len(obj.address) > 0:
            address = obj.address
        if len(obj.city) > 0:
            if len(address) > 0:
                address += ", "
            address += obj.city
        if len(obj.zip) > 0:
            if len(address) > 0:
                address += ", "
            address += obj.zip
        return address

    client_address.short_description = 'Adresse'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ['client', 'type', 'status', 'date']
    ordering = ('-date',)
    list_display = ('date', 'client', 'status', 'type', 'order')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['label', 'amount']
    ordering = ('label',)
    list_display = ('label', 'amount')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ['client', 'type', 'date']
    ordering = ('-date',)
    list_display = ('date', 'client', 'amount', 'type')


class OrderDataInline(admin.TabularInline):
    model = Order.articles.through
    extra = 1
    verbose_name = "ligne de commande"


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDataInline,
    ]
    list_display = ('date', 'client', 'status', 'order_total')
    list_filter = ['client', 'date']
    ordering = ('-date',)

    def order_total(self, obj):
        return obj.get_total

    order_total.short_description = 'Total'


admin.site.register(Order, OrderAdmin)
