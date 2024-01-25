from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extentions= ['.jpeg' , '.png' , '.jpg']
    if not ext.lower() in valid_extentions:
        raise ValidationError ('unsupported file extention (format)')


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar= models.FileField(upload_to='files/user_avatar/',validators=[validate_file_extension] , null=False , blank=False)
    description=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self) :
        return self.user.first_name
    
class Article(models.Model):
    title=models.CharField(max_length=100 , null=False , blank=False)
    cover=models.FileField(upload_to='files/article_cover/',validators=[validate_file_extension] ,null=False , blank=False )
    content= RichTextField()
    created_at = models.DateTimeField(default=datetime.now)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    author=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    promote= models.BooleanField(default=False)
    def __str__(self) :
        return self.title
    
class Category(models.Model):
    title=models.CharField(max_length=100)
    cover=models.FileField(upload_to='files/category_cover/' , validators=[validate_file_extension])    
    def __str__ (self):
        return self.title

    
