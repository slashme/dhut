from django.urls import path, include

from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

admin.autodiscover()

import dhut.views

urlpatterns = [
    path("", dhut.views.index, name="index"),
    path("add/", dhut.views.add, name="add"),
    path("line_chart/", dhut.views.line_chart, name="line-chart"),
    path("admin/", admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
]
