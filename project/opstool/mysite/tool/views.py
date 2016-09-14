from django.http import *
import datetime
from django.shortcuts import render,redirect
from django.template import RequestContext
from tool.models import *


def home(request):
    context = {}
    return render(request, 'home.html', context)