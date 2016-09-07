from tool.models import *

def get_roles(role_id = None, name = None):
	is_role_id_none = role_id == None
	is_name_none = name == None

	if not is_role_id_none and not is_name_none:
		role_object = Role.objects.filter(id = role_id,name = name)
		role_dict = {}
		role_dict['id'] = role_object.id
		role_dict['name'] = role_object.name

	elif not is_role_id_none and is_name_none:
		role_object = Role.objects.filter((id = role_id)
				role_dict = {}
				role_dict['id'] = role_object.id
				role_dict['name'] = role_object.name
		
			elif is_role_id_none and not is_name_none:
				role_object = Role.objects.filter(name = name)
				role_dict = {}
				role_dict['id'] = role_object.id
				role_dict['name'] = role_object.name
		
			return role_dict
		

def set_role()