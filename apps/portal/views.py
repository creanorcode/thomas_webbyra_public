from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.crm.models import QuoteRequest, ContactMessage

@login_required
def dashboard(request):
    # Visa användarens kopplade ärenden (om de finns)
    quotes = QuoteRequest.objects.filter(user=request.user).order_by("-created_at")
    contacts = ContactMessage.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "portal/dashboard.html", {"quotes": quotes, "contacts": contacts})
