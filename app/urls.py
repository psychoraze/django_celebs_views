from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("create/", CelebrityCreate.as_view(), name="create"),
    path("delete/<int:pk>", CelebrityDelete.as_view(), name="delete"),
    path("update/<int:pk>", CelebrityUpdate.as_view(), name="update"),
    path("detail/<int:pk>", CelebrityDetail.as_view(), name="detail"),
]
