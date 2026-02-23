from django.urls import path
from . import views

app_name = "crm"

urlpatterns = [
    path("kontakt/", views.contact, name="contact"),
    path("offert/", views.quote, name="quote"),
    path("tack/", views.thanks, name="thanks"),
]
