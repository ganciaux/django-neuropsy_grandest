from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from neuropsy.forms.client import NameForm
from neuropsy.models import Client

def index(request):
    form = NameForm()
    return render(request, 'client/index.html', {'form': form})


def search(request):
    name = request.GET.get('name', None)
    data = {
        'exists': Client.objects.filter(first_name__iexact=name).exists(),
        'name': name
    }
    return JsonResponse(data)