from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^blog/(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
    url(r'^blog/(?P<pk>\d+)/del$', views.post_del, name='post_del'),   
    url(r'^blog/new/$', views.post_new, name='post_new'),
    url(r'^blog/tag/(?P<id>\d+)/$',  views.tag_filter, name='tag_filter'),
    url(r'^archive/', views.archive, name='archive'),
    url(r'^search_by_day/', views.search_by_day, name='search_by_day'),
    url(r'^search_by_month/', views.search_by_month, name='search_by_month'),
    url(r'^search_by_year/', views.search_by_year, name='search_by_year'),

)

