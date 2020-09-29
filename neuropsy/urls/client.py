from django.urls import path

from neuropsy.views import client

app_name = 'client'
urlpatterns = [
    path('', client.index, name='index'),
    path('details/<int:client_id>', client.details, name='details'),
    path('search', client.search, name='search'),
]