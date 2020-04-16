from django.shortcuts import render
from django.http import JsonResponse
from .models import Event

# Create your views here.

def index(request):
    events = Event.objects.order_by("event_time")
    return JsonResponse({})
