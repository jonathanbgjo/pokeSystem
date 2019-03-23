
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.poke),
    url(r'^givepoke/(?P<user_id>\d+)$', views.give),
]
