from django.urls import path, include

from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

admin.autodiscover()

import dhut.views

urlpatterns = [
    path("", dhut.views.index, name="index"),
    path("add/", dhut.views.add, name="add"),
    path("index/", dhut.views.index, name="index"),
    path("db/", dhut.views.db, name="db"),
    path("db1/", dhut.views.db1, name="db1"),
    path("db2/", dhut.views.db2, name="db2"),
    path("db3/", dhut.views.db3, name="db3"),
    path("line_chart/", dhut.views.line_chart, name="line-chart"),
    path("line_chart1/", dhut.views.line_chart1, name="line-chart1"),
    path("line_chart2/", dhut.views.line_chart2, name="line-chart2"),
    path("line_chart3/", dhut.views.line_chart3, name="line-chart3"),
    path("admin/", admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
]
