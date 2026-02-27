from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("tjanster/", views.services, name="services"),
    path("tjanster/webbdesign/", views.service_web_design, name="service_web_design"),
    path("tjanster/webbhotell/", views.service_hosting, name="service_hosting"),
    path("tjanster/doman/", views.service_domain, name="service_domain"),
    path("tjanster/allt-i-ett/", views.service_bundle, name="service_bundle"),
    path("case/", views.cases, name="cases"),
    path("case/<slug:slug>/", views.case_detail, name="case-detail"),
    path("paket/", views.packages, name="packages"),
    path("om/", views.about, name="about"),
]
