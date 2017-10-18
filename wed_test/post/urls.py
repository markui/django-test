from django.conf.urls import url
from .views import post_list, post_detail, post_create, post_delete

app_name = 'post'

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='detail'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<pk>\d+)/delete/$', post_delete, name='delete'),
]