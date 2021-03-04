from django.urls import path
from .views import CategoryList, PostList, posts_by_category, CategoryDetail, PostDetail

urlpatterns = [
    path('category/all/', CategoryList.as_view()),
    path('category/detail/<int:pk>/', CategoryDetail.as_view()),
    path('post/all/', PostList.as_view()),
    path('post/detail/<int:pk>/', PostDetail.as_view()),
    path('post/category/<int:pk>/', posts_by_category),
]
