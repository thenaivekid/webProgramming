from django.urls import path
from . import views

# helps to prevent namespace collision by specifying the location
app_name = "todo"  
urlpatterns = [
    path("", views.index, name = "index"),
    path("add/", views.add, name = "add"),
]