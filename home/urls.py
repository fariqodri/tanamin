from .views import index, submit_tanaman, app
from django.urls import path, re_path

app_name = "home"
urlpatterns = [
  path('', app, name="index"),
  path('app/', index, name="app"),
  path('tanaman/', submit_tanaman, name="submit_tanaman")
]