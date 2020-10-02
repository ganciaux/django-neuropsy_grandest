from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from datetime import datetime
from neuropsy.forms.appointment import searchForm
from neuropsy.models import Appointment


def index(request):
    context = {
        'form': searchForm()
    }
    return render(request, 'appointment/index.html', context)


def details(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    context = {
        'appointment': appointment,
        'appointment_data': appointment.get_all_fields(),
        'error_message': "Le rendez-vous n'existe pas.",
    }
    return render(request, 'appointment/details.html', context)


def search(request):
    context = {}
    search_dates_time = {}
    search_dates = {
        'from': request.GET.get('date_from', None),
        'to': request.GET.get('date_to', None)
    }
    if Appointment.get_datetimes(search_dates, search_dates_time):
        if search_dates_time['from'] <= search_dates_time['to']:
            appointments = Appointment.objects\
                .exclude(date__lte=search_dates_time['from'])\
                .exclude(date__gte=search_dates_time['to'])
            if len(appointments) > 0:
                context = {
                    'appointments': appointments,
                }
            return render(request, 'appointment/list.html', context)
    else:
        context = {
            'message': 'Erreur de date: de \'' + search_dates['from'] + '\' à \'' + search_dates['to'] + '\'',
            'type': 'primary'
        }
    return render(request, 'alert.html', context)
