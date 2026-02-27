from django.shortcuts import render
from django.http import Http404


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


CASES = [
    {
        "slug": "thomas-webbyra",
        "title": "Thomas Webbyrå - fullstack byråplattform",
        "summary": "Django-plattform med CRM, kundportal och admin-workflow.",
    },
]


def cases(request):
    return render(request, "pages/cases.html", {"cases": CASES})


def case_detail(request, slug: str):
    case = next((c for c in CASES if c ["slug"] == slug), None)
    if not case:
        raise Http404
    return render(request, "pages/case_detail.html", {"case": case})
