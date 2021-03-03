from django.db import models
from django.conf import settings

# Create your models here.


class Candy(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
