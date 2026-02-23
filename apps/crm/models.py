from django.conf import settings
from django.db import models

class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ("new", "Ny"),
        ("in_progress", "Pågående"),
        ("closed", "Stängd"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contact_messages",
    )
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    internal_note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.subject} – {self.email}"


class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ("new", "Ny"),
        ("in_progress", "Pågående"),
        ("sent", "Skickad"),
        ("won", "Vunnen"),
        ("lost", "Förlorad"),
    ]

    SERVICE_CHOICES = [
        ("webbdesign", "Webbdesign"),
        ("hosting", "Webbhotell"),
        ("doman", "Domän"),
        ("allt", "Allt-i-ett"),
    ]

    BUDGET_CHOICES = [
        ("<5k", "< 5 000 kr"),
        ("5-15k", "5 000 – 15 000 kr"),
        ("15-30k", "15 000 – 30 000 kr"),
        ("30k+", "30 000+ kr"),
        ("unsure", "Osäker"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="quote_requests",
    )

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=120, blank=True)

    service = models.CharField(max_length=20, choices=SERVICE_CHOICES, default="allt")
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, default="unsure")
    deadline = models.DateField(null=True, blank=True)

    description = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    internal_note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Offert – {self.name} ({self.get_service_display()})"
