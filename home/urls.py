from .views import index, submit_tanaman
from django.urls import path, re_path

app_name = "home"
urlpatterns = [
  path('', index, name="index"),
  path('tanaman/', submit_tanaman, name="submit_tanaman")
]