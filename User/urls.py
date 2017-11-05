from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^$', 'User.views.Index', name='Index'),
  url(r'^login/$', 'django.contirb.auth.views.login',{'template_name':'User/login.html'}, name='userLogin'),
  

]

