from rest_framework import serializers
from ring.models import Article
from django.contrib.auth.models import User

class ArticleSrializer(serializers.ModelSerializer):
    class Meta:
       model = Article
       fields = "__all__"
       # fields = ("title" , "slug" , "author" , "content" , "publish" , "status")
       #exclude = ("created" , "updated")


class UserSrializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = "__all__"       