from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("tjanster/", views.services, name="services"),
    path("paket/", views.packages, name="packages"),
    path("om/", views.about, name="about"),
]
