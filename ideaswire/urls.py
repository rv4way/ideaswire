from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^image-processing/face/add', include('add_image.urls')),
    url(r'^image-processing/face/status', include('check_status.urls')),
    url(r'^image-processing/search', include('search_image.urls')),

]
