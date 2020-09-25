from django.urls import path

from neuropsy.views import client

app_name = 'client'
urlpatterns = [
    path('', client.index, name='index'),
]