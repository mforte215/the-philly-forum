from django.shortcuts import render
from .models import Article
import logging

def IndexView(request):
    if request.method == 'GET':
        top_post = Article.objects.filter(top_post=True)
        article_list = Article.objects.filter(draft=False).filter(top_post=False)
        return render(request, 'app/index.html', {'top_post': top_post, 'articles': article_list, })

def ArticleDetailView(request, slug):
    if request.method == 'GET':
        article = Article.objects.get(slug=slug)
        return render(request, 'app/article-detail.html', {'article': article})
