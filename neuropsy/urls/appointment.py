from django.urls import path

from neuropsy.views import appointment

app_name = 'appointment'
urlpatterns = [
    path('', appointment.index, name='index'),
    path('details/<int:appointment_id>', appointment.details, name='details'),
    path('search', appointment.search, name='search'),
]