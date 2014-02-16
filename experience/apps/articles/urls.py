from django.conf.urls import patterns, include, url

from experience.apps.articles import views

urlpatterns = patterns('',
    url(r'^$', views.render_home, name='home'),
    url(r'^(?P<id>[a-z0-9]+)/(?P<name>[a-z_-]+)/$', views.render_homepage, name='homepage'),
    url(r'^(?P<id>[a-z0-9]+)/(?P<name>[a-z_-]+)/articles/$', views.render_articles, name='articles'),
    url(r'^(?P<id>[a-z0-9]+)/(?P<name>[a-z_-]+)/edit/$', views.render_edit, name='edit'),
)