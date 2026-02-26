from django.conf import settings
from django.db import models


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_profile",
    )

    company = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"CustomerProfile: {self.user.username}"
