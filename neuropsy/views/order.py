from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from datetime import datetime
from neuropsy.forms.order import searchForm
from neuropsy.models import Order


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
    return render(request, 'order/index.html', context)


def details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {
        'order': order,
        'order_data': order.get_all_fields(),
        'error_message': "La commande n'existe pas.",
    }
    return render(request, 'order/details.html', context)


def search(request):
    if date_validate(request.GET.get('date_from', None))==True and date_validate(request.GET.get('date_to', None))==True:
        date_from = datetime.strptime(request.GET.get('date_from', None), "%d-%m-%Y %H:%M")
        date_to = datetime.strptime(request.GET.get('date_to', None), "%d-%m-%Y %H:%M")
        orders = Order.objects.exclude(date__lte=date_from).exclude(date__gte=date_to)
        if len(orders) > 0:
            context = {
                'orders': orders,
                'error_message': "La commande n'existe pas.",
            }
            return render(request, 'order/list.html', context)
        context = {
            'message': 'Aucune commande',
            'type': 'primary'
        }
    
    context = {
            'message': 'Erreur de date',
            'type': 'primary'
        }
    return render(request, 'alert.html', context)
