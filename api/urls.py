from django.urls import path
from .views import CategoryList, PostList

urlpatterns = [
    path('category/all', CategoryList.as_view(), name='listpost'),
    path('post/all', PostList.as_view(), name='listpost'),
]
