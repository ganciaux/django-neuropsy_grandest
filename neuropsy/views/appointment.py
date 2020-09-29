from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from neuropsy.forms.appointment import NameForm
from neuropsy.models import Appointment


def index(request):
    context = {
        'form': NameForm()
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
    date_from = request.GET.get('date_from', None)
    date_to = request.GET.get('date_to', None)
    appointments = Appointment.objects.exclude(date__lte=date_from).filter(date__gte=date_to)
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
    return render(request, 'alert.html', context)
