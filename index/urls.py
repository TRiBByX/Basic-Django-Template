from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.Index.as_view(), name='index'),
    url(r'^del', views.DeactivateItem.as_view(), name='delItem'),
    url(r'^test', views.DBtest.as_view(), name='test'),
    url(r'^update', views.UpdateProjectName.as_view(),
        name='UpdateProjectName'),
]
