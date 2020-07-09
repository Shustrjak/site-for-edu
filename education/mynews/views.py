from django.shortcuts import render
from .forms import ArticleForm, AuthorForm
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


def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'all_news.html', context={'all_articles': articles})


def create_article(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'create_article.html', context={"form": form})
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_article.html', context={"form": form})


def delete_article(request, pk):
    if request.method == 'GET':
        article = Article.objects.filter(pk=pk).first()
        form = ArticleForm(instance=article)
        return render(request, 'delete_article.html', context={"form": form})
    elif request.method == 'POST':
        article = Article.objects.filter(pk=pk).first()
        form = ArticleForm(instance=article)
        if article:
            article.delete()
        return render(request, 'delete_article.html', context={"form": form})


def edit_article(request, pk):
    if request.method == 'GET':
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        return render(request, 'update_article.html', context={"form": form})
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'update_article.html', context={"form": form})

def show_article(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    return render(request, 'show_article.html',context={"form": form})
