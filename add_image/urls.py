from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.accept_req, name='accept_req'),
]