from django.views.generic import ListView
from .models import Article
from django.shortcuts import render
from .models import Product


class ArticleSearchView(ListView):
    model = Article
    template_name = 'met_1/article_search.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(title__icontains=query)
        return Article.objects.all()



def search_view(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()
    return render(request, 'met_1/article_search.html', {'articles': articles})



def get_queryset(self):
    query = self.request.GET.get('q ')
    if query:
        return Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return Article.objects.all()


def product_list(request):
    products = Product.objects.all()
    return render(request, '/templates/catalog/product_list.html', {'products': products})









