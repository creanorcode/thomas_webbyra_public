from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return [
            "pages:home",
            "pages:services",
            "pages:packages",
            "pages:about",
            "pages:cases",
            "pages:service_web_design",
            "pages:service_hosting",
            "pages:service_domain",
            "pages:service_bundle",
        ]

    def location(self, item):
        return reverse(item)
