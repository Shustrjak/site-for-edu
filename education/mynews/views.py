from django.shortcuts import render
from .forms import ArticleForm, AuthorForm
from .models import Article, Author
from django.views.generic import TemplateView, CreateView, DetailView
from django.views.generic.base import View
from django.views.generic.list import ListView


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
    return render(request, 'all_authors.html', context={'all_articles': articles})


def create_article(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'create_author_form.html', context={"form": form})
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_author_form.html', context={"form": form})


def delete_article(request, pk):
    if request.method == 'GET':
        article = Article.objects.filter(pk=pk).first()
        form = ArticleForm(instance=article)
        return render(request, 'delete_author.html', context={"form": form})
    elif request.method == 'POST':
        article = Article.objects.filter(pk=pk).first()
        form = ArticleForm(instance=article)
        if article:
            article.delete()
        return render(request, 'delete_author.html', context={"form": form})


def edit_article(request, pk):
    if request.method == 'GET':
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        return render(request, 'update_author.html', context={"form": form})
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'update_author.html', context={"form": form})


def show_article(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    return render(request, 'author_detail.html', context={"form": form})


class CreateAuthorView(View):

    def get(self, request):
        form = AuthorForm()
        return render(request, 'mynews/create_author_form.html', context={"form": form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'mynews/create_author_form.html', context={"form": form})

class AllAuthorsTemplateView(TemplateView):
    template_name = 'mynews/all_authors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.all()
        context.update({"authors": authors})
        return context

class AuthorDetailView(DetailView):

    model = Author

class AuthorCreateView(CreateView):

    model = Author
    fields = '__all__'
    success_url = '/cb_all_authors/'

    def get_success_url(self):
        return f'/cb_detail/{self.object.pk}'

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    paginate_by = 5
