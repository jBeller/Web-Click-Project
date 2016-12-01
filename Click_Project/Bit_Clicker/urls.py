from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game$', views.game, name='game'),
    url(r'^game/$', views.game, name='game'),
    url(r'^register$', views.register, name='register'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login$', views.login_view, name='login_view'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^save$', views.save_view, name='save_view'),
    url(r'^save/$', views.save_view, name='save_view'),
]
