from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        article_data =[]
        articles= Article.objects.all().order_by('-created_at')[:9]
        for article in articles:
            article_data.append({
                
                    'title':article.title,
                    'cover':article.cover.url,
                    'category':article.category.title,
                    'created':article.created_at.date,
                    'author' : article.author.user.username
                
            })
        context = {
            'article_data':article_data
        }     
        return render(request, 'index.html', context)