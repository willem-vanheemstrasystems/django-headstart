from django.conf.urls import url
from . import views

# Register your url patterns here.
urlpatterns = [
	url(r'^$', views.index, name='index'),
]