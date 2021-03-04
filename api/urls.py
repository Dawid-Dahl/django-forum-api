from django.urls import path
from .views import CategoryList, CreateCategory, PostList, posts_by_category, CategoryDetail, PostDetail, replies_by_post

urlpatterns = [
    path('category/all/', CategoryList.as_view()),
    path('category/detail/<int:pk>/', CategoryDetail.as_view()),
    path('category/create/', CreateCategory.as_view()),
    path('post/all/', PostList.as_view()),
    path('post/detail/<int:pk>/', PostDetail.as_view()),
    path('post/category/<int:pk>/', posts_by_category),
    path('post/replies/<int:pk>/', replies_by_post),
]
