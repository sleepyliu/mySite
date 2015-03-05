from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.blog, name='blog'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<title_id>\d+)/$', views.detail, name='detail'),
    url(r'^archive/', views.archive, name='archive'),

)