from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html")

def services(request):
    return render(request, "pages/services.html")

def packages(request):
    return render(request, "pages/packages.html")

def about(request):
    return render(request, "pages/about.html")
