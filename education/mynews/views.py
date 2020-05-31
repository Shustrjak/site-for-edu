from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


def index_view(request):
    article = Article.objects.get(pk=1)
    context = {
        'article': article,
        'all_articles': Article.objects.all(),
    }
    return render(request, 'mynews/index.html', context=context)
