from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from apps.pages.sitemaps import StaticViewSitemap

sitemaps = {"static": StaticViewSitemap()}

urlpatterns += [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.pages.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("crm/", include("apps.crm.urls")),
    path("portal/", include("apps.portal.urls")),
]
