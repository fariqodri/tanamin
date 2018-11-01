from django.urls import path
from .views import constraint_graph
urlpatterns = [
    path("graph", constraint_graph)
]