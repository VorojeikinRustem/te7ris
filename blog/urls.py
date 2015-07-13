
from django.conf.urls import url

from blog.views import articles, article, about


urlpatterns = [
    url(r'^(\d+)/$', articles),
    url(r'^(?P<month>\d+)/(?P<year>\d+)/$', articles),
    url(r'^articles/(?P<article_id>\d+)/$', article, name='article'),
    url(r'^about/$', about, name='about'),
    url(r'^$', articles, name='articles'),
]
