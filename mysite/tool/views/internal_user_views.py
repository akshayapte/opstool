from django.http import *
import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from tool.models import *
from tool.db_api.auth_db import *

	
def dashboard(request):
    context = {}
    auth_dict = get_user(request)
    context['auth_dict'] = auth_dict
    return render(request, 'internal_user/dashboard.html', context)
