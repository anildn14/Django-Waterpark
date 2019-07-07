# from django.core.validators import validate_email
from django.db import models


class PhoneNumberField(models.CharField):
	description="Field to validate phonenumber"
	def __init__(self, *args,**kwargs):
		kwargs['max_length']=5
		super(PhoneNumberField,self).__init__(*args,**kwargs)