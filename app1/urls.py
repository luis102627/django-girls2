from django.conf.urls import url
from app1.views import listaPost, sendid, Lista2

urlpatterns = [
	url(r'^lista/', Lista2.as_view(),name='listado'),
    url(r'^detalle/(?P<id>[\d]+)', sendid,name='detalle'),
]