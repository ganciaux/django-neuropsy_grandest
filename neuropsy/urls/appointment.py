from django.urls import path

from neuropsy.views import appointment

app_name = 'appointment'
urlpatterns = [
    path('', appointment.index, name='index'),
]