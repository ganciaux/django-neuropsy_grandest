from django.contrib import admin
from .models import Appointment, Client

admin.site.register(Client)
admin.site.register(Appointment)
