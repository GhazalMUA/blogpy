
from django.urls import path
from . import views

urlpatterns = [   
    path('', views.IndexPage.as_view(), name='index'),
    path('detail/<int:int>' , views.DetailView.as_view(), name='detail'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('about/' , views.AboutPage.as_view(), name='about'),
    path('article/' , views.SimpleArticleAPIView.as_view(), name='simple_article'),
    path('article/search/' ,views.SearchContentAPIView.as_view(), name='search_article'),
    path('articles/all/' , views.ArticleAPIview.as_view() , name='articleAPI'),
    path('article/submit/' , views.SubmitArticleAPIView.as_view(), name='submit'),
    path('article/update-cover/' , views.UpdateCoverAPIview.as_view(), name='update_cover'),
    path('article/delete/' , views.DeleteArticleAPIView.as_view() , name='article_delete'),
    ##api namayesh tamame userha
    path('hameuserhaAPI/', views.AllUsersAPI.as_view()),
    ##django list view mvt
    path('listarticles', views.ListArticlesMVT.as_view(), name='listarticles'),
    ###api namayeshe taki user ha ba estefade az id shon
    
    path('hameuserhaAPI/<int:pk>' , views.NamayeshtakiUserAPI.as_view(), name ='namayeshtaki'),
    path('listarticles/<int:pk>' , views.TakMaghaleMVT.as_view(), name ='TakMaghaleMVT'),
]
   