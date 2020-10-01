from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from neuropsy.forms.client import searchForm
from neuropsy.models import Client


def index(request):
    context = {
        'form': searchForm(),
        'clients': Client.objects.order_by('first_name')
    }
    return render(request, 'client/index.html', context)


def details(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    context = {
        'client': client,
        'client_data': client.get_all_fields(),
        'error_message': "Le client n'existe pas.",
    }
    return render(request, 'client/details.html', context)


def search(request):
    name = request.GET.get('name', None)
    email = request.GET.get('email', None)
    clients = Client.objects.filter(first_name__contains=name).filter(email__contains=email)
    if len(clients) > 0:
        context = {
            'clients': clients,
            'error_message': "Le client n'existe pas.",
        }
        return render(request, 'client/list.html', context)
    context = {
        'type': 'primary',
        'message': "Aucun client",
    }
    return render(request, 'alert.html', context)