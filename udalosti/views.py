from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Speaker, Conference, Session


# Home view
def home(request):
        conferences = Conference.objects.all()
        context = {
            'nadpis': 'Konferenční zasedání',
            'conferences': conferences
        }
        return render(request, 'home.html', context=context)


class SessionListView(ListView):
        model = Session
        template_name ='session/list.html'
        context_object_name ='session_list'


class SessionDetailView(DetailView):
        model = Session
        template_name ='session/detail.html'
        context_object_name ='session'