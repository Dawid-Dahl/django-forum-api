from django.db.models import fields
from rest_framework import serializers
from candy.models import Candy
from django.conf import settings


class CandySerializer(serializers.ModelSerializer):
    class Meta:
        model = Candy
        fields = ("id", "title", "price")
