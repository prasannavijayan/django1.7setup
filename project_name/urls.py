from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import settings

urlpatterns = patterns('',
    # static website URL's
    url(r'^$', TemplateView.as_view(template_name="website/index.html")),

    # admin interface URL
    url(r'^admin/', include(admin.site.urls)),

    # application URL's
)
