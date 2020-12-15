from django.urls import path

from neuropsy.views import payment

app_name = 'payment'
urlpatterns = [
    path('', payment.index, name='index'),
    path('details/<int:payment_id>', payment.details, name='details'),
    path('search', payment.search, name='search'),
]