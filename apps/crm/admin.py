from django.contrib import admin
from .models import ContactMessage, QuoteRequest

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "subject", "email", "status")
    list_filter = ("status", "created_at")
    search_fields = ("email", "subject", "message", "name")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "email", "service", "budget", "status")
    list_filter = ("status", "service", "budget", "created_at")
    search_fields = ("email", "name", "company", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
