from django.urls import path

from neuropsy.views import order

app_name = 'order'
urlpatterns = [
    path('', order.index, name='index'),
    path('details/<int:order_id>', order.details, name='details'),
    path('search', order.search, name='search'),
]