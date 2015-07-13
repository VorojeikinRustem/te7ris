from django.conf.urls import url

from views import dashboard, documents

urlpatterns = [
    # url(r'^(\d+)/$', articles),
    # url(r'^(?P<month>\d+)/(?P<year>\d+)/$', articles),
    # url(r'^about/$', about, name='about'),

    url(r'^(?P<collection>[\w.-]+)/$', documents, name='documents'),
    url(r'^$', dashboard, name='dashboard'),
]
