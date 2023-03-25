# from django.shortcuts import render
from ring.models import Article
from django.contrib.auth.models import User
from .serializers import (
    ArticleSrializer,
    UserSrializer
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    # ListAPIView,
    # CreateAPIView,
    # RetrieveAPIView,
    # UpdateAPIView,
    # DestroyAPIView,
)
# from rest_framework.permissions import IsAdminUser
from .permissions import IsAthorOrReadOnly , IsStaffOrReadOnly , IsSuperUserStaffReadOnly
# Create your views here.
#list view api

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSrializer
    
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSrializer 
    permission_classes = (IsAthorOrReadOnly , IsStaffOrReadOnly)
    # lookup_field = 'slug'

# list view api user

# class ArticleList(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSrializer

# class ArticleCreate(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSrializer

# class ArticleRetrieve(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSrializer
#     lookup_field = 'slug'

# class ArticleUpdate(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSrializer
#     lookup_field = 'slug'

# class ArticleDestroy(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSrializer
#     lookup_field = 'slug'



class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSrializer
    permission_classes = (IsSuperUserStaffReadOnly,)
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSrializer 
    permission_classes = (IsSuperUserStaffReadOnly,)