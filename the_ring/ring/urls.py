from django.urls import path , include
from .views import ArticleList , ArticleDetali , UserDetali , UserList

app_name = "ring"

urlpatterns = [
    path("" , ArticleList.as_view() , name= 'list'),
    path("<int:pk>" , ArticleDetali.as_view() , name= 'detail'),
    path("users/" , UserList.as_view() , name= 'user-list'),
    path("users/<int:pk>" , UserDetali.as_view() , name= 'user-detail'),
]

