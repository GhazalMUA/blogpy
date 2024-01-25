from django.contrib import admin
from .models import UserProfile , Article , Category


class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'avatar' , 'description']
    search_fields=('user',)
    list_per_page= 2

class ArticleAdmin(admin.ModelAdmin):
    list_display =['title','created_at','author','promote', 'cover']
    search_fields=('title',)
    list_per_page= 10


class CategoryAdmin(admin.ModelAdmin):
    list_display =['title','cover']
    list_per_page= 3


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
