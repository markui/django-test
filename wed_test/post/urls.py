from django.conf.urls import url
from .views import post_list

app_name = 'post'

urlpatterns = [
    url(r'^$', post_list, name='list'),

]