from __future__ import unicode_literals

from datetime import datetime, date
from django.db import models
import re
import bcrypt
# Create your models here.
class UserManager(models.Manager):
	def loginVal(self, postData):
		results = {
			'status': True,
			'errors': [],
			'user': None
		}

		users = self.filter(email_address = postData['email_address'])

		#if self.filter(email_address = postData['email_address']).count()<1: #of User.objects.filer().count()
		if len(users) < 1:
			results['status'] = False
		else:
			if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
				results['user'] = users[0]
			else: 
				results['status'] = False
		return results


	def creator(self, postData):
		user = self.create(name = postData['name'], alias = postData['alias'], email_address = postData['email_address'], password = bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt()))
		return user
	def validate(self, postData):
		results = {
			'status': True,
			'errors': []
		}
		if len(postData['name']) < 3:
			results['errors'].append('YOU SHALL NOT PASS: First name too short')
			results['status'] = False
		if not postData['name'].isalpha():
			results['errors'].append('YOU SHALL NOT PASS: Use only characters for first name')
			results['status'] = False
		if len(postData['alias']) < 3:
			results['errors'].append('YOU SHALL NOT PASS: alias too short')
			results['status'] = False
		if not postData['alias'].isalpha():
			results['errors'].append('YOU SHALL NOT PASS: Use only characters for alias')
			results['status'] = False
		if not re.match("[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]", postData['email_address']):
			results['errors'].append('YOU SHALL NOT PASS: Email not valid')
			results['status'] = False
		if postData['password'] != postData['c_password']:
			results['errors'].append('YOU SHALL NOT PASS: Passwords do not match')
			results['status'] = False
		if len(postData['password']) < 8:
			results['errors'].append('YOU SHALL NOT PASS: Password too short')
			results['status'] = False
		if self.filter(email_address = postData['email_address']).count()>0: #of User.objects.filer().count()
			results['errors'].append('YOU SHALL NOT PASS: Email already taken')
			results['status'] = False
		if datetime.strptime("01/11/1917",  "%d/%m/%Y") > datetime.strptime(postData['dob'], "%Y-%m-%d"):
			results['errors'].append('YOU SHALL NOT PASS: Cannot be born in the past')
			results['status'] = False
		if datetime.strptime(postData['dob'], "%Y-%m-%d") > datetime.now():
			results['errors'].append('YOU SHALL NOT PASS: Cannot be born in the future')
			results['status'] = False
		return results
		
class User(models.Model):
	name = models.CharField(max_length = 255)
	alias = models.CharField(max_length = 255)
	email_address = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	objects = UserManager()
