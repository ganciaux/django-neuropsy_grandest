from django.shortcuts import get_object_or_404, render
from datetime import datetime
from neuropsy.models import Article


def index(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'article/index.html', context)

def details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
        'article_data': article.get_all_fields(),
        'error_message': "L'article n'existe pas.",
    }
    return render(request, 'article/details.html', context)
