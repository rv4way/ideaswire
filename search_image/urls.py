from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.search_image, name='search_image'),
]