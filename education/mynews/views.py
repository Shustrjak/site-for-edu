from django.shortcuts import render

from .models import Article, Author


def index_view(request):
    article = Article.objects.get(pk=1)
    author = Author.objects.get(pk=1)
    context = {
        'article': article,
        'all_articles': Article.objects.all(),
        'author': author,
        'all_authors': Author.objects.all(),
    }
    return render(request, 'mynews/index.html', context=context)
