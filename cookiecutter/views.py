from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from cookiecutter.models import Cutter


class CutterListView(ListView):

    model = Cutter

    def get_context_data(self, **kwargs):
        context = super(CutterListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CutterDetailView(DetailView):

    model = Cutter

    def get_context_data(self, **kwargs):
        context = super(CutterDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
