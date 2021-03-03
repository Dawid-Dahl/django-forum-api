from api.views import GetAllCandy
from django.urls import path

urlpatterns = [
    path("candy/all/", GetAllCandy.as_view())
]
