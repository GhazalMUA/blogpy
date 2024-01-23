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
        promote_list=[]    
        all_promote_article=Article.objects.filter(promote=True)    
        for promote_article in all_promote_article:
            promote_list.append({
                'category':promote_article.category ,
                'author': promote_article.author.user.first_name + " " + promote_article.author.user.last_name ,
                'cover' : promote_article.cover.url ,
                'title' : promote_article.title ,

            })

        context = {
            'promote_list' : promote_list ,
            'article_data':article_data
        }     
        return render(request, 'index.html', context)

class ContactPage(TemplateView):
    template_name= 'page-contact.html'