from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class RoomsList(ListView):
    models = Room
    template_name = 'chat.html'
    context_object_name = 'rooms'
    queryset = Room.objects.all()

class MessagesList(ListView):
    models = Messages
    template_name = 'chat.html'
    context_object_name = 'messages'
    queryset = Messages.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context