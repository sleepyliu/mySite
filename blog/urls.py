from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<title_id>\d+)/$', views.detail, name='detail'),
    url(r'^archive/', views.archive, name='archive'),
    url(r'^search_by_day/', views.search_by_day, name='search_by_day'),
    url(r'^search_by_month/', views.search_by_month, name='search_by_month'),
    url(r'^search_by_year/', views.search_by_year, name='search_by_year'),

)
