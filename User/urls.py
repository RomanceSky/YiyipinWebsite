from django.conf.urls import url

from .views import *
app_name = 'User'
urlpatterns = [
  url(r'^$', Index),
  url(r'^login/$', 'django.contirb.auth.views.login',{'template_name':'User/login.html'}, name='userLogin'),
  
  url(r'^list/$',index, name='index'),
]

