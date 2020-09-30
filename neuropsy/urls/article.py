from django.urls import path

from neuropsy.views import article

app_name = 'article'
urlpatterns = [
    path('', article.index, name='index'),
    path('details/<int:article_id>', article.details, name='details'),
]