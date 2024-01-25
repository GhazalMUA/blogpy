from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# from django.http.response import status
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
        all_promote_article=Article.objects.filter(promote=True).order_by('title')  
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
    
class AboutPage(TemplateView):
    template_name='page-about.html'    

 
########
       

class ArticleAPIview(APIView): 
    def get(self, request, format=None):
        try:
           data= []
           all_articles_api = Article.objects.all()[:20]
           for article in all_articles_api:
               data.append({
                'title':article.title,
                'content':article.content,
                'category':article.category.title,
                'author':article.author.user.username,
                })
#dar ghesmate try say mikonim ye kari ro anjam bedim va age karemoon be moshkel barbokhore on varede vexcept mishe.
        
            
           return Response({'data':data} , status=status.HTTP_200_OK)
        except:
           return Response({'status':'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


########search tooye title e maghaleha ba estefade az serializer
        

class SimpleArticleAPIView(APIView):
    def get (self,request, format=None):
        article_title= request.GET['article_title']
        article= Article.objects.filter(title__contains=article_title)
        serialized_data= serializers.SingleArticleSerializer(article, many=True)
        data= serialized_data.data
        try:
            return Response({'data':data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

########### search tooye content e maghaleha bokone        
        
class SearchContentAPIView(APIView):
    
    def get(self,request,format=None):
        try:
            from django.db.models import Q

            query=request.GET['query']
            articles=Article.objects.filter(Q(content__icontains=query))
            data = []
            for article in articles:
                data.append({
                    'title': article.title,
                    'content' : article.content,
                    'category' : article.category.title,
                    'author': article.author.user.first_name + ' ' + article.author.user.last_name ,
                })
            return Response ({'data':data}, status=status.HTTP_200_OK)
        except:
            return Response({'status':'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 





#######submit a article 
class SubmitArticleAPIViws(APIView):
    def post(self,request,format=None):
        try:
            serializer=serializers.SubmitArticleSerializer(data=request.data)
            if serializer.is_valid():
                title=serializer.data.get('title')
                cover=request.FILES['cover']
                category_id=serializer.data.get('category_id')
                content= serializer.data.get('content')
                author_id=serializer.data.get('author_id')
                promote=serializer.data.get('promote')
            else:    
                return Response ({'status':'bad'}, status=status.HTTP_200_OK)
            
            user=User.objects.get(id=author_id)
            author=UserProfile.objects.get(user=user)
            category=Category.objects.get(id=category_id)

            article=Article()
            article.title=title
            article.cover=cover
            article.category=category
            article.content=content
            article.author=author
            article.promote=promote
            article.save()
            return Response({'status':'ok'}, status=status.HTTP_200_OK)
            
            












        except:
            return Response({'status':'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
                    



#######update  a cover in articles
class UpdateCoverAPIview(APIView):
    def post(self,request,format=None):
        try:
        #    begir=request.GET['article_id']
        #    moredenazar=Article.objects.filter(article_id='article_id')
            serializer= serializers.UpdateCoverSerializer(data=request.data)
            if serializer.is_valid():
                article_id=serializer.data.get('article_id')
                cover=request.FILES['cover']
                # moredenazar=Article()
                # article_id='article_id'
                # cover= 'cover'
                # moredenazar.save()
            else:
                return Response({'status':'kharab kardi'}, status=status.HTTP_200_OK)
            Article.objects.filter(id=article_id).update(cover=cover)
            return Response ({'status':'ok'}, status=status.HTTP_200_OK )
        except:
            return Response({'status':'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        