from django.conf.urls import url

from .views import *

urlpatterns = [
  url(r'^$', Index),
  url(r'^login/$', 'django.contirb.auth.views.login',{'template_name':'User/login.html'}, name='userLogin'),
  
  url(r'^User/list/$', index1, name='test')
]

