from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^resume/$',views.resume, name='index'),
    url(r'^$',views.home, name='index'),
]
