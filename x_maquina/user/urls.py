from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from user.forms import LoginForm

urlpatterns = [
    url(r'^login/$', auth_views.login,
        {'template_name': 'user/login.html',
         'authentication_form': LoginForm}, name='Login'),
    url(r'^logout/$',
        views.user_logout, name='Logout'),
    url(r'^new/$', views.registrate, name='Registrate'),
]
