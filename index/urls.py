from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.Index.as_view(), name='index'),
    url(r'^del', views.DeactivateItem.as_view(), name='delItem'),
]
