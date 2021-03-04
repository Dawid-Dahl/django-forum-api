from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    country = CountryField(default="SE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = CountryField(default="SE")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def increment_views(self):
        """ triggered each time a user visits the detail view for a post. Increments the views_count for the post """
        pass

    def get_latest_response_date(self):
        """ date of last response to this post. This is only applicable to Parent posts and not response """
        pass

    def get_responses(self):
        """ Returns a list of posts which has the current post as parent, if the post doesnt have any responses return Post.objects.none. If the post has a parent (is a response), return None """
        pass

    def count_responses(self):
        """ Number of responses connected to this post """
        pass

    def get_latest_response_date2(self):
        """ Return the created_at date for the latest response connected to this post """
        pass
