# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
import django
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import validate_slug,validate_email
from .validators import validate_domainonly_email,validate_image_ext,validate_integers
from .fields import PhoneNumberField

class UserManager(BaseUserManager):
	def create_user(self,username,email,first_name=None,last_name=None,gender=None,age=None,marital_status=None,mobile_number=None,password=None,is_active=True,is_staff=False,is_admin=False):
		user_obj=self.model(
			email=self.normalize_email(email)
			)
		user_obj.set_password(password)
		user_obj.staff=is_staff
		user_obj.admin=is_admin
		user_obj.active=is_active
		user_obj.username=username
		user_obj.first_name=first_name
		user_obj.last_name=last_name
		user_obj.gender=gender
		user_obj.age=age
		user_obj.marital_status=marital_status
		user_obj.mobile_number=mobile_number
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self,username,email,first_name,last_name,gender,age,marital_status,mobile_number,password=None):
		user=self.create_user(username,email,first_name,last_name,gender,age,marital_status,mobile_number,password=password,is_staff=True)
		return user

	def create_superuser(self,username,email,first_name,last_name,gender,age,marital_status,mobile_number,password=None):
		user=self.create_user(username,email,first_name,last_name,gender,age,marital_status,mobile_number,password=password,is_staff=True,is_admin=True)
		return user

class User(AbstractBaseUser):
	username 		=models.CharField(max_length=50)
	email 			=models.EmailField(max_length=255)#,unique=True)
	active 			=models.BooleanField(default=True)
	staff 			=models.BooleanField(default=False)
	admin 			=models.BooleanField(default=False)
	first_name 		=models.CharField(max_length=20,null=True)
	last_name 		=models.CharField(max_length=20,null=True)
	GENDER_CHOICES 	=(('M', 'Male'),('F', 'Female'),('O', 'Other'))
	gender 			= models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
	age 			=models.DateField(max_length=10,null=True)#,null=False,validators=[validate_integers])
	marital_status	=models.CharField(max_length=10,null=True)
	mobile_number	=models.CharField(max_length=15,unique=True,validators=[validate_integers],null=True)
	timestamp		=models.DateTimeField(auto_now_add=True)
	# now email will be used as username
	# email and password will be required by default
	USERNAME_FIELD='username'
	# USERNAME_FIELD='email'
	# REQUIRED_FIELDS=['email']#,'first_name','last_name','gender','age','marital_status','mobile_number']
	
	objects= UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.first_name+self.last_name

	def get_short_name(self):
		return self.first_name

	def has_perm(self,perm,obj=None):
		return True

	def has_perms(self, perm_list, obj=None):
		"""
		Return True if the user has each of the specified permissions. If
		object is passed, check if the user has all required perms for it.
		"""
		return all(self.has_perm(perm, obj) for perm in perm_list)


	def has_module_perms(self,app_label):
		if self.is_active and self.is_admin:
			return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active
	

	'''
	from migrations....these are the defaut field created
	('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
	('password', models.CharField(max_length=128, verbose_name='password')),
	('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
	'''
class Park_Details(models.Model):
	park_name=models.CharField(max_length=250)
	park_address=models.TextField(max_length=1000)
	park_time=models.CharField(max_length=50)
	# park_logo=models.CharField(max_length=1000)
	park_logo=models.ImageField(upload_to="Images/",default="Images/None/new-img.jpg",validators=[validate_image_ext])
	park_docs=models.FileField(upload_to="Docs/",default="Docs/None/new-doc")
	park_url=models.CharField(max_length=250,unique=True)
	park_price=models.CharField(max_length=250)
	park_likes=models.IntegerField(default=0)
	is_fav=models.BooleanField(default=False)

	# Video No:30
	def get_absolute_url(self): #reverse is used so that after clicking on submit form where the page needs to be redirected
		return reverse('water_park:detail',kwargs={'pk' : self.pk})
	def __str__(self):
		return self.park_name + ' - ' + self.park_address

class Images(models.Model):
	park=models.ForeignKey(Park_Details,on_delete=models.CASCADE)
	image_name=models.CharField(max_length=250)
	image_url=models.FileField(validators=[validate_image_ext])
	
	#for form : refer video 33
	# def get_absolute_url(self):
	# 	return reverse('water_park:detail',kwargs={'pk' : self.park.id})
	def __str__(self):
		return self.image_name

class Comment_Details(models.Model):
	comment_name=models.CharField(max_length=50)
	comment_email_id=models.EmailField(max_length=250,validators=[validate_domainonly_email])#,validators=[validate_email]) #or use email field
	comment_text=models.TextField(max_length=1000)
	comment_time=models.DateTimeField(default=django.utils.timezone.now)

