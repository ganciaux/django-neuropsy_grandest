from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from datetime import datetime
from neuropsy.forms.appointment import searchForm
from neuropsy.models import Appointment


def date_validate(date_text, format='%d-%m-%Y %H:%M'):
    try:
        if date_text != datetime.strptime(date_text, format).strftime(format):
            raise ValueError
        return True
    except ValueError:
        return False

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
    if date_validate(request.GET.get('date_from', None))==True and date_validate(request.GET.get('date_to', None))==True:
        date_from = datetime.strptime(request.GET.get('date_from', None), "%d-%m-%Y %H:%M")
        date_to = datetime.strptime(request.GET.get('date_to', None), "%d-%m-%Y %H:%M")
        appointments = Appointment.objects.exclude(date__lte=date_from).exclude(date__gte=date_to)
        if len(appointments) > 0:
            context = {
                'appointments': appointments,
                'error_message': "Le rendez-vous n'existe pas.",
            }
            return render(request, 'appointment/list.html', context)
        context = {
            'message': 'Aucun rendez-vous',
            'type': 'primary'
        }
    
    context = {
            'message': 'Erreur de date',
            'type': 'primary'
        }
    return render(request, 'alert.html', context)
