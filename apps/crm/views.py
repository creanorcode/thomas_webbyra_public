from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ContactForm, QuoteForm


def _maybe_attach_user(request, instance):
    if request.user.is_authenticated:
        instance.user = request.user
    return instance


def _notify_admin(subject: str, body: str):
    if settings.ADMIN_NOTIFY_EMAIL:
        send_mail(
            subject=subject,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_NOTIFY_EMAIL],
            fail_silently=True,
        )


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            msg = form.save(commit=False)
            msg = _maybe_attach_user(request, msg)
            msg.save()

            messages.success(request, "Tack! Ditt meddelande är mottaget. Jag återkommer så snart jag kan.")

            _notify_admin(
                subject=f"[Thomas Webbyrå] Ny kontakt: {msg.subject}",
                body=f"Namn: {msg.name}\nE-post: {msg.email}\n\nMeddelande:\n{msg.message}",
            )
            return redirect("crm:thanks")
        messages.error(request, "Oj! Något blev fel i formuläret. Kontrollera fälten och försök igen.")
    return render(request, "crm/contact.html", {"form": form})


def quote(request):
    form = QuoteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            quote_obj = form.save(commit=False)
            quote_obj = _maybe_attach_user(request, quote_obj)
            quote_obj.save()

            messages.success(request, "Tack! Din offertförfrågan är skickad. Jag hör av mig med nästa steg.")

            _notify_admin(
                subject=f"[Thomas Webbyrå] Ny offertförfrågan: {quote_obj.name}",
                body=(
                    f"Namn: {quote_obj.name}\nE-post: {quote_obj.email}\nTelefon: {quote_obj.phone}\n"
                    f"Företag: {quote_obj.company}\nTjänst: {quote_obj.get_service_display()}\n"
                    f"Budget: {quote_obj.get_budget_display()}\nDeadline: {quote_obj.deadline}\n\n"
                    f"Beskrivning:\n{quote_obj.description}"
                ),
            )
            return redirect("crm:thanks")
        messages.error(request, "Oj! Något blev fel i formuläret. Kontrollera fälten och försök igen.")
    return render(request, "crm/quote.html", {"form": form})


def thanks(request):
    return render(request, "crm/thanks.html")
