from django import forms
from .models import ContactMessage, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 6}),
        }

class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ["name", "email", "phone", "company", "service", "budget", "deadline", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 7}),
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
