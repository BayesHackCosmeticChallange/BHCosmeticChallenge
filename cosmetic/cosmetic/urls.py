from django.conf.urls import patterns, include, url
from django.contrib import admin
from chart.views import render_chart
from main.views import main


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cosmetic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chart/$', render_chart),
    url(r'main/', main),
)