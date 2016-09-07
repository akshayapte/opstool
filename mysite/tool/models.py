from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import m2m_changed

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	def __str__(self):
		return str(self.first_name) + str(self.last_name)

class Role(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)


class UserRole(models.Model):
	user = models.ForeignKey(User)
	role = models.ForeignKey(Role)
	def __str__(self):
		return str(self.user) + str(self.role)

class Product(models.Model):
	product_name = models.CharField(max_length=200)
	carrier = models.CharField(max_length=200)
	def __str__(self):
		return str(self.product_name)