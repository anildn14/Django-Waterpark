# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Park_Details,Images,Comment_Details
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User=get_user_model()

'''
#search option in admin page of users
class UserAdmin(admin.ModelAdmin):
	search_fields=['email']
	form = UserAdminChangeForm 		#edit/update view
	add_form=UserAdminCreationForm	#create view 
	# class Meta:
	# 	model = User
'''

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username','mobile_number','admin')
    list_filter = ('admin','staff','active') #right side table contains these filters
    fieldsets = (
        ('Main Info', {'fields': ('email', 'password')}), #If main info is kept none then that row wont appear in admin page.....main info appears as table heading
        ('Personal info', {'fields': ('username','email','password','first_name','last_name','gender','age','marital_status','mobile_number')}), #add fields to show in personal info
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','username') # add parameters by which you want to search in the page
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Park_Details)
admin.site.register(Images)
admin.site.register(Comment_Details)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)