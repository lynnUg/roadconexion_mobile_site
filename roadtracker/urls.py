from django.conf.urls import patterns, include, url
from django.views.generic import (TemplateView,ListView)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='front.html')),
    url(r'', include('social_auth.urls')),
    # url(r'^$', 'roadtracker.views.home', name='home'),
    # url(r'^roadtracker/', include('roadtracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'profile_images/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )