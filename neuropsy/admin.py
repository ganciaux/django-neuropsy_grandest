from django.contrib import admin
from .models import Appointment, Client, Article, Order, OrderData, Payment


admin.site.site_header = "Neuropsy Grand-Est"
admin.site.site_title = "Neuropsy Grand-Est"
admin.site.index_title = "Administration du site Neuropsy Grand-Est"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_filter = ['origin']
    list_per_page = 100


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ['date', 'type', 'client']
    raw_id_fields = ["client"]
    list_per_page = 100


admin.site.register(Article)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ['date', 'type', 'client']
    list_per_page = 100


class OrderDataInline(admin.TabularInline):
    model = Order.articles.through
    extra = 1
    verbose_name = "ligne de commande"


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDataInline]


@admin.register(Order)
class OrderAdmin(OrderAdmin):
    list_filter = ['date', 'status', 'client']
    list_per_page = 100
    readonly_fields = ('is_finished',)

    def is_finished(self, obj):
        return obj.status == 'FINISHED'

    is_finished.boolean = True
