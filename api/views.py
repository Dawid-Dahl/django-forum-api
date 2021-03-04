from django.db.models.fields import NullBooleanField
from django.views import generic
from rest_framework import viewsets, filters, generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from forum.models import Post, Category
from .serializers import CategorySerializer, PostSerializer
from rest_framework.decorators import api_view

# Create your views here.


class CategoryList(generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveAPIView):

    serializer_class = CategorySerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Category, id=item)


class PostList(generics.ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, id=item)


@api_view(["GET"])
def posts_by_category(request, pk):
    data = PostSerializer(Post.objects.filter(
        category=pk, parent__isnull=True), many=True).data
    return Response(data)


@api_view(["GET"])
def replies_by_post(request, pk):
    data = PostSerializer(Post.objects.filter(
        parent=pk), many=True).data
    return Response(data)
