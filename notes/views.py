from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.
def index(request):
    context = { 'note': Note.objects.all()}

    return HttpResponse((context, request))
