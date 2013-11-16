from django.conf.urls import patterns, include, url
from django.views.generic import (TemplateView,ListView)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from mobile.models import Report
urlpatterns = patterns('',
    # Examples:
     url(r'^view_reports$', ListView.as_view(queryset=Report.objects.all().order_by('-created_on'),
        template_name='posts.html',
        paginate_by=15, allow_empty=True)),
    url(r'^add_report/$',
        'mobile.views.submit_report',
        name='add_report'),
    url(r'^roadtracker/$', TemplateView.as_view(template_name='stylish-portfolio.html')),
    url(r'^$', TemplateView.as_view(template_name='front.html')),
    url(r'', include('social_auth.urls')),
    # url(r'^$', 'roadtracker.views.home', name='home'),
    # url(r'^roadtracker/', include('roadtracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
      url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^',  include('registration.backends.default.urls')),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^search/$',
        'mobile.views.search',
        name='search'),
     url(r'^report/$',
        'mobile.views.report',
        name='report'),
     url(r'^follow/$',
        'mobile.views.follow',
        name='follow'),

)
if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'profile_images/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )