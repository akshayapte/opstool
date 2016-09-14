from django.conf.urls import url,include
from django.contrib import admin
from tool.views.internal_user_views import dashboard
urlpatterns = [
	url(r'^dashboard/', dashboard, name = 'dashboard' ),
]