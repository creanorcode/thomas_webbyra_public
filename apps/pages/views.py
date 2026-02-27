from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def services(request):
    return render(request, "pages/services.html")


def service_web_design(request):
    return render(request, "pages/services/web_design.html")


def service_hosting(request):
    return render(request, "pages/services/hosting.html")


def service_domain(request):
    return render(request, "pages/services/domain.html")


def service_bundle(request):
    return render(request, "pages/services/bundle.html")


def packages(request):
    return render(request, "pages/packages.html")


def about(request):
    return render(request, "pages/about.html")
