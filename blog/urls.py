#imort url functions
from django.conf.urls import url, include
#import views functions
from . import views
#used for login handlings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_view, name='post_view'),
    url(r'^post/add/$', views.addpost, name='addpost'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page':'/'}, name='logout'),

]
