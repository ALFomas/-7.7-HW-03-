from django.urls import path
from .views import (
    PostList,
    PostDetail,
    SearchList,
    NewsCreate,
    NewsUpdate,
    NewsDelete,
    ArticlesCreate,
    ArticlesUpdate,
    ArticlesDelete,
)

urlpatterns = [

    path('', PostList.as_view(), name='post_list'),
    path('search', SearchList.as_view(), name='search_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
]
