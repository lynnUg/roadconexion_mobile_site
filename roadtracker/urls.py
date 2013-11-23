from django.conf.urls import patterns, include, url
from django.views.generic import (TemplateView,ListView)
from rest_framework import viewsets, routers

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from mobile.models import Report
from registration.views import (RegistrationView,ActivationView)
urlpatterns = patterns('',
    # Examples:
     url(r'^view_reports$', ListView.as_view(queryset=Report.objects.all().order_by('-created_on'),
        template_name='posts.html',
        paginate_by=15, allow_empty=True)),
    url(r'^add_report/$',
        'mobile.views.submit_report',
        name='add_report'),
    url(r'^roadconexion/$', TemplateView.as_view(template_name='stylish-portfolio.html')),
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
     url(r'^delete/(\d+)/$',
        'mobile.views.delete',
        name='delete_story'),
      url(r'^getuser/$',
        'mobile.views.profile',
        name='get_profile'),
      url(r'^view_reports/(\w+)$',
        'mobile.views.reports_sorted',
        name='reports_sorted'),

      url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

      #new urls
      #url(r'^reports/$', 'mobile.views.report_list'),
      #url(r'^reports/(?P<pk>[0-9]+)/$', 'mobile.views.report_detail'),
      #url(r'^report_list/$',
      #  'mobile.views.report_list',
       # name='report_list')
      

)
if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'profile_images/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )





urlpatterns = patterns('mobile.views',
   url(r'^reports/$', 'report_list'),
   url(r'^reports/(?P<pk>[0-9]+)/$', 'report_detail'),
)

