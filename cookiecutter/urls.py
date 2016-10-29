from django.conf.urls import url

from cookiecutter.views import CutterDetailView, CutterListView

from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$',
        CutterDetailView.as_view(), name='cutter-detail'),
    url(r'^$', CutterListView.as_view(), name='cutter-list'),
]
