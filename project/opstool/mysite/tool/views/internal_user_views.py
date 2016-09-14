from django.http import *
import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from tool.models import *
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from tool.db_api.auth_db import *
import MySQLdb

@csrf_exempt	
def dashboard(request):
	auth_dict = get_user(request)
	if auth_dict['logged_in'] == False:
		raise Http404
	
	if request.method == 'GET':
		page_type = 0
		context = {}
		
		context['auth_dict'] = auth_dict
		context['page_type'] = page_type
		if 'msisdn' in request.GET:
			page_type = 1
			msisdn_details = get_msisdn_details(request.GET['msisdn'])
			msisdn_details_dict = {}
			for row in msisdn_details:
				msisdn_details_dict['msisdn'] = str(row[3])
				msisdn_details_dict['subscription_id'] = str(row[0])
				msisdn_details_dict['customer_id'] = str(row[1])
				msisdn_details_dict['subscription_status_id'] = str(row[10])
				msisdn_details_dict['start_date'] = str(row[11])
				msisdn_details_dict['create_date'] = str(row[32])
				


			context['msisdn_details'] = msisdn_details_dict
			context['page_type'] = page_type
			context['auth_dict'] = auth_dict
			
		return render(request, 'internal_user/dashboard.html', context)
	
def get_msisdn_details(msisdn):
	db = MySQLdb.connect("localhost","root","root","baas")
	cursor = db.cursor()
	cursor.execute("select * from user_subscription where msisdn = '%s'"%(msisdn))
	data = cursor.fetchall()
	db.close()
	return data
