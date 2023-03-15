from django.shortcuts import render  , get_object_or_404
from django.views.generic import ListView , DeleteView
from .models import Article
from django.contrib.auth.models import User
# Create your views here.
class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.all()
    

class ArticleDetali(DeleteView):
    def get_object(self):
        return get_object_or_404(Article.objects.all(),
        pk =self.kwargs.get('pk'))
    
class UserList(ListView):
    def get_queryset(self):
        return User.objects.all()
    

class UserDetali(DeleteView):
    def get_object(self):
        return get_object_or_404(User.objects.all(),
        pk =self.kwargs.get('pk'))    