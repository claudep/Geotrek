from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$',        'caminae.core.views.home', name='home'),
    url(r'^login/$',  'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout',),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('caminae.core.urls', namespace='core', app_name='core')),
    url(r'', include('caminae.maintenance.urls', namespace='maintenance', app_name='maintenance')),
)

urlpatterns += staticfiles_urlpatterns()
