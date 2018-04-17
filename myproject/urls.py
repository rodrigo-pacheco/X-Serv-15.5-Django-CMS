from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'acorta.views.slash'),
    url(r'^(\d+)$', 'acorta.views.number'),
    url(r'(.*)', 'cms.views.content'),
    url(r'.*', 'acorta.views.notfound'),
)
