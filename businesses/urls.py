from django.conf.urls import url
from businesses import views

urlpatterns = [
    url(r'^create/$', views.business_create, name="create"),
    url(r'^detail/(?P<business_slug>[-\w]+)/$', views.business_detail, name="detail"),
    url(r'^list/$', views.business_list, name="list"),
    url(r'^update/(?P<business_slug>[-\w]+)/$', views.business_update, name="update"),
    url(r'^delete/(?P<business_slug>[-\w]+)/$', views.business_delete, name="delete"),
    ]
