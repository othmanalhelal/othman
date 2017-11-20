from django.conf.urls import url
from businesses import views

urlpatterns = [
    url(r'^create/$', views.business_create, name="create"),
    url(r'^detail/$', views.business_detail, name="detail"),
    url(r'^list/$', views.business_list, name="list"),
    url(r'^update/$', views.business_update, name="update"),
    url(r'^delete/$', views.business_delete, name="delete"),
    ]