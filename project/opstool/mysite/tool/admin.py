from django.contrib import admin
from tool.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Role)
admin.site.register(UserRole)
