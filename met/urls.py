from django.urls import path
from .views import ArticleSearchView
from  .views import product_list
urlpatterns = [
    path('search/', ArticleSearchView.as_view(), name='article_search'),
path('', product_list, name='product_list'),
]
