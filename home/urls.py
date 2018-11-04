from .views import index
from django.urls import path, re_path

urlpatterns = [
  re_path(r'$', index)
]