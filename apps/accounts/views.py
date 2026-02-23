from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.user.is_authenticated:
        return redirect("portal:dashboard")

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Välkommen! Du är nu inloggad.")
            return redirect("portal:dashboard")
        messages.error(request, "Inloggningen misslyckades. Kontrollera uppgifter och försök igen.")

    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "Du är nu utloggad.")
    return redirect("pages:home")
