from django.conf.urls import patterns, include, url
from django.contrib import admin
from chart.views import render_chart
from main.views import main
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cosmetic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chart/$', render_chart),
    url(r'main/', main),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)