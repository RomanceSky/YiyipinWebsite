from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', blog_index),
    url(r'^list/$', blog_index1,  name='blog_index')

]
