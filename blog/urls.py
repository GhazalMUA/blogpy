
from django.urls import path
from . import views

urlpatterns = [   
    path('', views.IndexPage.as_view(), name='index'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('about/' , views.AboutPage.as_view(), name='about'),
    path('article/' , views.SimpleArticleAPIView.as_view(), name='simplearticle'),
    path('article/search/' ,views.SearchContentAPIView.as_view(), name='search_article'),
    path('articles/all/' , views.ArticleAPIview.as_view() , name='articleapi'),
    path('article/submit/' , views.SubmitArticleAPIViws.as_view(), name='submit'),
    path('article/update-cover/' , views.UpdateCoverAPIview.as_view(), name='update-cover'),
]
