from django.urls import path
from .views import CategoryList, PostList, PostsByCategory

urlpatterns = [
    path('category/all', CategoryList.as_view()),
    path('post/all', PostList.as_view()),
    path('post/category/<int:pk>', PostsByCategory.as_view()),
]
