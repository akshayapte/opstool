from tool.models import *

def get_user(request):
	msg = 'Incorrect login details'
	if 'login' in request.POST:
		request.session['user'] = {'logged_in':False, 'msg': msg}
		username = request.POST['username']
		password = request.POST['password']

		

		if User.objects.filter(username=username,password=password).exists():
			user_obj = User.objects.get(username=username,password=password)
			
			request.session['user']['user_name'] = username
			request.session['user']['logged_in'] = True
			request.session['user']['first_name'] = user_obj.first_name
			request.session['user']['last_name'] = user_obj.last_name
			
			user_roles = UserRole.objects.filter(user__id = user_obj.id)

			for user_role_obj in user_roles:
				if(user_role_obj.role.name == 'internal'):
					request.session['user']['login_type'] = 'internal_user'
				if(user_role_obj.role.name == 'external'):
					request.session['user']['login_type'] = 'external_user'



			
			request.session['user']['id'] = user_obj.id
			request.session.modified = True
		else:
			msg = 'Incorrect Details'
			request.session['user']['msg'] = msg


		
	if not 'user' in request.session:
		request.session['user'] = {'logged_in':False, 'msg': msg}
		request.session.modified = True
	return request.session['user']


def set_logout(request):
	request.session['user']={'logged_in':False}	