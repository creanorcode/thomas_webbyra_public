from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("offert/<int:pk>/", views.quote_detail, name="quote_detail"),
    path("kontakt/<int:pk>/", views.contact_detail, name="contact_detail"),
]
