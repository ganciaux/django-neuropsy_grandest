from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from datetime import datetime
from neuropsy.forms.payment import NameForm
from neuropsy.models import Payment


def date_validate(date_text, format='%d-%m-%Y %H:%M'):
    try:
        if date_text != datetime.strptime(date_text, format).strftime(format):
            raise ValueError
        return True
    except ValueError:
        return False


def index(request):
    context = {
        'form': NameForm()
    }
    return render(request, 'payment/index.html', context)


def details(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    context = {
        'payment': payment,
        'payment_data': payment.get_all_fields(),
        'error_message': "Le paiement n'existe pas.",
    }
    return render(request, 'payment/details.html', context)


def search(request):
    if date_validate(request.GET.get('date_from', None))==True and date_validate(request.GET.get('date_to', None))==True:
        date_from = datetime.strptime(request.GET.get('date_from', None), "%d-%m-%Y %H:%M")
        date_to = datetime.strptime(request.GET.get('date_to', None), "%d-%m-%Y %H:%M")
        payments = Payment.objects.exclude(date__lte=date_from).exclude(date__gte=date_to)
        if len(payments) > 0:
            context = {
                'payments': payments,
                'error_message': "Le paiement n'existe pas.",
            }
            return render(request, 'payment/list.html', context)
        context = {
            'message': 'Aucun paiement',
            'type': 'primary'
        }
    
    context = {
            'message': 'Erreur de date',
            'type': 'primary'
        }
    return render(request, 'alert.html', context)
