from django.contrib import admin
from .models import Candy

# Register your models here.


class CandyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Candy)
