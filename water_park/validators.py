from django.core.validators import validate_slug,validate_email
from django.utils.translation import ugettext_lazy as _
from django import forms
import os

VALID_EMAIL_TYPES=[".in",".com",".edu"]
def validate_domainonly_email(value):
	# if file_type not in IMAGE_FILE_TYPES:
	if not value.endswith(tuple(VALID_EMAIL_TYPES)):
	# if value.endswith() not in VALID_EMAIL_TYPES:
		raise forms.ValidationError("Email should end with .in, .com or .edu")
	# if not ".in" in value:
	# 	raise forms.ValidationError(_("Email should end with .in"))
	return value

BLACKLIST=['test']
def validate_blacklisted(value):
	if value in BLACKLIST:
		raise forms.ValidationError(_("Sorry, this value is not valid."))
	return value


VALID_IMAGE_TYPES=[".png",".jpg",".jpeg"]
def validate_image_ext(value):
	ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
	if not ext.lower() in VALID_IMAGE_TYPES:
		raise forms.ValidationError("Images should be in .png, .jpg or .jpeg format.")
	return value
	
'''def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')'''

def validate_integers(value):
	if not value.isdigit() or value==str(0):
		raise forms.ValidationError(_("Sorry, this value is not valid."))
	return value