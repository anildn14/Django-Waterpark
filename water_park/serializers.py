from rest_framework import serializers
from .models import Park_Details
from django.db import models
from .validators import validate_image_ext

#modelname+Serializer
class Park_DetailsSerializer(serializers.ModelSerializer):

	park_logo=serializers.ImageField(max_length=None,use_url=True)
	park_docs=serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model=Park_Details
		# fields=('park_name','park_address','park_price','park_logo','park_docs')
		fields='__all__'
