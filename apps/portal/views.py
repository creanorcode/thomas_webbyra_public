from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from apps.crm.models import QuoteRequest, ContactMessage


def _require_owner_or_staff(request, obj):
    """
    Allow:
    - Staff isers (admin/support)
    - the owner (obj.user == request.user)
    If obj.user is None, only staff can view.
    """
    if request.user.is_staff:
        return

    if getattr(obj, "user_id", None) != request.user.id:
        raise Http404("Not found")


@login_required
def dashboard(request):
    # Visa användarens kopplade ärenden (om de finns)
    quotes = QuoteRequest.objects.filter(user=request.user).order_by("-created_at")
    contacts = ContactMessage.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "portal/dashboard.html", {"quotes": quotes, "contacts": contacts})


@login_required
def quote_detail(request, pk: int):
    quote = get_object_or_404(QuoteRequest, pk=pk)
    _require_owner_or_staff(request, quote)
    return render(request, "portal/quote_detail.html", {"quote": quote})


@login_required
def contact_detail(request, pk: int):
    contact = get_object_or_404(ContactMessage, pk=pk)
    _require_owner_or_staff(request, contact)
    return render(request, "portal/contact_detail.html", {"contact": contact})
