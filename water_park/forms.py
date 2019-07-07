from django.contrib.auth.models import User
from .models import Images,Park_Details,Comment_Details
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import validate_slug,validate_email
from .validators import validate_domainonly_email,validate_blacklisted
from django.forms.widgets import DateInput



User=get_user_model()

class UserForm(forms.ModelForm):
	### You can override the fields behaviour here
	email = forms.EmailField(validators=[validate_domainonly_email]) #unique=True
	username=forms.CharField(label="user",widget=forms.TextInput(attrs={"placeholder":"Your Username"}),validators=[validate_blacklisted])
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta: #info about your class is metaclass
		model=User
		# fields='__all__'
		fields=['username','email','first_name','last_name','password','gender','age','marital_status','mobile_number']
		labels = {'age': ('D.O.B'),}
		widgets = {'age': DateInput(attrs={'type': 'date'})}


	'''
	# def clean_<my_filed_name>:
	def clean_username(self,*args,**kwargs):
		#field level validation
		username=self.cleaned_data.get('username')
		if not "*" in username:
			raise forms.ValidationError("This is not a proper username. Not contains *")
		else:
			return username

	# You can override email properties by adding it above with username.
	# But if you want to keep the properties and add new properties then just do validation.
	def clean_email(self,*args,**kwargs):
		#field level validation
		email=self.cleaned_data.get('email')
		if not email.endswith(".com"):
			raise forms.ValidationError("Email should end with .com")
		else:
			return email
	'''
	'''def clean(self,*args,**kwargs): #calling the default method of clean
		# form level validation
		cleaned_data=super(UserForm, self).clean()
		email=cleaned_data.get('email')
		if not ".com" in email:
			raise forms.ValidationError("Email should end with .com")
		else:
			return email'''

class UserAdminCreationForm(forms.ModelForm):
	"""A form for creating new users. Includes all the required
	fields, plus a repeated password."""
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','gender','age','marital_status','mobile_number')
		
	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

	

class UserAdminChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','gender','age','marital_status','mobile_number', 'password', 'active', 'admin')

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial["password"]


class Park_DetailsForm(forms.ModelForm):
	
	park_price=forms.DecimalField()
	class Meta:
		model = Park_Details
		fields=['park_name','park_address','park_time','park_logo','park_url','park_price']


class ImagesForm(forms.ModelForm):

	class Meta: #info about your class is metaclass
		model=Images
		# fields='__all__'
		fields=['image_name','image_url']

class Comment_DetailsForm(forms.ModelForm):

	class Meta:

		model=Comment_Details
		# model._meta.get_field('comment_email_id')._unique = True  #user can comment n no.of times
		fields=['comment_name','comment_email_id','comment_text']

