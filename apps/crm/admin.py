from django.contrib import admin
from django.utils import timezone
from .models import ContactMessage, QuoteRequest

@admin.action(description="Markera som: Pågående")
def mark_in_progress(modeladmin, request, queryset):
    for obj in queryset:
        obj.set_status("in_progress")
        obj.save()

@admin.action(description="Markera som: Stängd")
def mark_closed(modeladmin, request, queryset):
    for obj in queryset:
        obj.set_status("closed")
        obj.save()

@admin.action(description="Markera som: Skickad offert (sent)")
def mark_sent(modeladmin, request, queryset):
    for obj in queryset:
        obj.set_status("sent")
        obj.save()

@admin.action(description="Tilldela mig (assigned_to=request.user)")
def assign_to_me(modeladmin, request, queryset):
    queryset.update(assigned_to=request.user)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "subject", "email", "status")
    list_filter = ("status", "created_at")
    search_fields = ("email", "subject", "message", "name")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    actions = [assign_to_me, mark_in_progress, mark_closed]

    def save_model(self, request, obj, form, change):
        # if status changed in admin form, update timestamp properly
        if change and "status" in form.changed_data:
            obj.set_status(form.cleaned_data["status"])
        super().save_model(request, obj, form, change)


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "name",
        "email",
        "service",
        "budget",
        "status",
        "assigned_to",
        "sent_to",
        "status_changed_at",
    )

    list_filter = (
        "status",
        "service", 
        "budget",
        "created_at",
        "assigned_to",
    )

    search_fields = ("email", "name", "company", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "sent_at", "status_changed_at")

    actions = [assign_to_me, mark_in_progress, mark_sent]

    def save_model(self, request, obj, form, change):
        if change and "status" in form.changed_data:
            obj.set_status(form.cleaned_data["status"])
        super().save_model(request, obj, form, change)
