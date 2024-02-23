from rest_framework import serializers
from .models import *

class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2000)
    created_at = serializers.DateTimeField(required=True)





class SubmitArticleSerializer(serializers.Serializer):
    title=serializers.CharField(required=True, allow_null=False, allow_blank=False,max_length=200)
    cover=serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    category_id=serializers.IntegerField(required=True, allow_null=False)
    content=serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2000)
    author_id=serializers.IntegerField(required=True, allow_null=False)
    promote=serializers.BooleanField(required=True, allow_null=False)


class UpdateCoverSerializer(serializers.Serializer):
    article_id=serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=200)
    cover=serializers.FileField(required=True, allow_null=False, allow_empty_file=False)


class DeleteArticleSerializer(serializers.Serializer):
    article_id=serializers.IntegerField(required=True, allow_null=False)






class UserProfileAPISerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields ='__all__'
