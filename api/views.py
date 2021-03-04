from rest_framework import viewsets, filters, generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from forum.models import Post, Category
from .serializers import CategorySerializer, PostSerializer

# Create your views here.


class CategoryList(generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostList(generics.ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostsByCategory(generics.RetrieveAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
