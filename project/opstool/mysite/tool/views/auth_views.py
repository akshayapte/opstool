from django.shortcuts import render,redirect
from tool.db_api.auth_db import *
from django.views.decorators.csrf import csrf_exempt

def home(request):
	context = {}
	auth_dict = get_user(request)
	print auth_dict
	if auth_dict['logged_in']:
		if auth_dict['login_type'] == 'internal_user':
			return redirect('/internal_user/dashboard/')
		elif auth_dict['login_type'] == 'external_user':
			return redirect('/external_user/dashboard/')
	return render(request,'home.html',context)

@csrf_exempt
def login(request):
	auth_dict = get_user(request)
	print auth_dict
	if auth_dict['logged_in']:
		if auth_dict['login_type'] == 'internal_user':
			return redirect('/internal_user/dashboard/')
		elif auth_dict['login_type'] == 'external_user':
			return redirect('/external_user/dashboard/')
		return render(request,'home.html',context)
	else:
		return render(request,'home.html', {'message': auth_dict['msg'] or 'Incorrect login details' })

def logout(request):
	set_logout(request)
	return redirect('/')
