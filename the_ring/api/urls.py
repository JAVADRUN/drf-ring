from django.urls import path
from .views import (
    ArticleList, 
    # ArticleDetail, 
    UserList, 
    UserDetail,
    ArticleUpdate,
    ArticleRetrieve,
    ArticleDestroy,        
    ArticleCreate,
)
app_name = "api"
urlpatterns = [
    path("" , ArticleList.as_view() , name= 'list'),
    path("create/<slug:slug>" , ArticleCreate.as_view() , name= 'create'),
    path("update/<slug:slug>" , ArticleUpdate.as_view() , name= 'update'),
    path("retrieve/<slug:slug>" , ArticleRetrieve.as_view() , name= 'retrieve'),
    path("destroy/<slug:slug>" , ArticleDestroy.as_view() , name= 'destroy'),
    # path("<slug:slug>" , ArticleDetail.as_view() , name= 'detail'),
    path("users/" , UserList.as_view() , name= 'user-list'),
    path("users/<int:pk>" , UserDetail.as_view() , name= 'user-detail'),

]
