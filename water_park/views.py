# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import View
from .models import Park_Details,Images,Comment_Details,User
from django.http import JsonResponse
from .forms import UserForm,ImagesForm,Park_DetailsForm,Comment_DetailsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin

#RESTAPI
from .serializers import Park_DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

#list all parkdetails or create a new park
#parks/

class Park_DetailsViewSet(viewsets.ModelViewSet):
	
	queryset=Park_Details.objects.all()
	serializer_class=Park_DetailsSerializer
	# permission_classes = [AllowAny]

	def get_permissions(self):
		print "self.action :",self.action
		if self.action == 'list':					#list all waterparks
			permission_classes = [AllowAny]
		elif self.action == 'create':				#create a new waterpark
			permission_classes = [IsAdminUser]
		elif self.action == 'retrieve':				#list a single waterpark
			permission_classes = [AllowAny]
		elif self.action == 'update':				#update a waterpark but have to send all the data
			permission_classes = [IsAdminUser]
		elif self.action == 'partial_update':		#update a waterpark but can send single data
			permission_classes = [IsAdminUser]
		elif self.action == 'destroy':				#delete a waterpark
			permission_classes = [IsAdminUser]
		elif self.action == 'hello':
			permission_classes = [AllowAny]
		else:
			permission_classes = [AllowAny]
		return [permission() for permission in permission_classes]

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class IndexView(generic.ListView):
	template_name="water_park/index.html"
	context_object_name="wp_list"

	def get_queryset(self):
		# return Park_Details.objects.all()
		return Park_Details.objects.order_by('park_name')

def index(request):
	park = Park_Details.objects.all()
	query = request.GET.get("q")
	if query:
		park = park.filter(
			Q(park_name__icontains=query) |
			Q(park_address__icontains=query)
		).distinct()
		print "query_park :",park
		print "query_park :",park == None
		print "park.count() :",park.count()
		if park.count()!=0:
			print "park :",park
			# print "park_name :",park.park_name
			print "park is available"
			return render(request, 'water_park/index.html', {'wp_list': park})
		else:
		# return render(request, 'music/index.html', {'albums': albums})
			return render(request, 'water_park/message.html', {'error_message': 'No Results found.'})
	else:
		# return render(request, 'music/index.html', {'albums': albums})
		return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_name')})


class DetailView(generic.DetailView):
	model=Park_Details
	template_name="water_park/detail.html"
	context_object_name="parkid"
		

class WaterParkCreate(CreateView):
	model=Park_Details
	fields=['park_name','park_address','park_time','park_logo','park_url','park_price']#,'park_likes','is_fav']  as these are not required while adding a wp

# @user_passes_test(lambda u:u.is_admin) #for super user
# @login_required(login_url='/waterparks/login_superuser')#for normal user
@login_required(login_url='water_park:login_superuser')
def create_waterpark(request):
	if not request.user.is_authenticated():
		return render(request,'water_park/login.html')

	else:
		if request.user.is_admin:
			form = Park_DetailsForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				park = form.save(commit=False)
				# album.user = request.user
				park.park_logo = request.FILES['park_logo']
				file_type = park.park_logo.url.split('.')[-1]
				file_type = file_type.lower()
				if file_type not in IMAGE_FILE_TYPES:
					context = {
						'park': park,
						'form': form,
						'error_message': 'Image file must be PNG, JPG, or JPEG',
					}
					return render(request, 'water_park/create_waterpark.html', context)
				park.save()
				return render(request, 'water_park/detail.html',{'parkid':park})
			context = {
				"form": form,
			}
			return render(request, 'water_park/create_waterpark.html', context)
		else:
			return render(request, 'water_park/message.html', {'error_message': 'User must be Super-User to Add WaterPark'})

class PermMixin(object):
	def get_object(self):
		if self.request.user.is_admin:
			print "self.request.user.is_admin :",self.request.user.is_admin
			print "self.request.user :",self.request.user
			return True
		print "self.request.user.is_admin :",self.request.user.is_admin
		print "self.request.user :",self.request.user
		logout(self.request) 
		return False
		# return render(self.request, 'water_park/message.html', {'error_message': 'User must be Super-User to delete comment.'})

class WaterParkUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#,UserPassesTestMixin,PermMixin,PermissionRequiredMixin
	# permission_required = 'has_module_perms'

	model=Park_Details
	fields=['park_name','park_address','park_time','park_logo','park_url','park_price']#,'park_likes','is_fav']  as these are not required while adding a wp


	# # @login_required(login_url=' 	water_park:login_superuser')
	def test_func(self):
		post=self.get_object()
		if self.request.user.is_admin:
			print "self.request.user.is_admin :",self.request.user.is_admin
			print "self.request.user :",self.request.user
			return True
		print "self.request.user :",self.request.user
		print "self.request.user.is_admin :",self.request.user.is_admin
		# logout(self.request) 
		return False
	# 	# return render(self.request, 'water_park/message.html', {'error_message': 'User must be Super-User to delete comment.'})

class WaterParkDelete(DeleteView):
	model=Park_Details
	success_url=reverse_lazy('water_park:index')
#ABOVE CODE IS FOR GENERIC VIEW ######

@login_required(login_url='water_park:login_superuser')
def delete_waterpark(request, park_id):
	if request.user.is_admin:
		park = Park_Details.objects.get(pk=park_id)
		park.delete()
		return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_name')})
	else:
		return render(request, 'water_park/message.html', {'error_message': 'User must be Super-User to delete waterpark'})

def add_comment(request):
	form = Comment_DetailsForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.save()
		return redirect('water_park:comments') # if not this methood it redirects to last page i.e. add-comment page

	else:
		context = {
			"form": form,}
		return render(request, 'water_park/add_comment.html', context)

# @login_required#(login_url='/waterparks/login_user')
# @user_passes_test(lambda u:u.is_admin)
@login_required(login_url='water_park:login_superuser')
def delete_comment(request,com_id):
	if request.user.is_admin:
		comment = Comment_Details.objects.get(pk=com_id)
		comment.delete()
		return render(request, 'water_park/comments.html', {'com_details':Comment_Details.objects.order_by('-comment_time')})
	else:
		return render(request, 'water_park/message.html', {'error_message': 'User must be Super-User to delete comment.'})

def comments(request):
	#3 different ways to reverse the list
	return render(request, 'water_park/comments.html',{'com_details':Comment_Details.objects.order_by('comment_time').reverse()})
	
def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
		"form": form,
	}
	return redirect('water_park:login_user')
	# return render(request, 'water_park/login.html', context)

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				wps = Park_Details.objects.order_by('park_name')
				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
				else:
					return redirect('water_park:index') # not below method : because if you login and press delete and if not admin you press back it redirects to login page
			else:
				return render(request, 'water_park/message.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'water_park/message.html', {'error_message': 'Invalid Login.'})

	return render(request, 'water_park/login.html')

def login_superuser(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_admin:
				print "Superrrrrrrrrr"
				login(request, user)
				wps = Park_Details.objects.order_by('park_name')
				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
					# return redirect(next_data)
				else:
					return render(request, 'water_park/index.html', {'wp_list': wps})
			else:
				return render(request, 'water_park/message.html', {'error_message': 'User must be Super-User'})
		else:
			return render(request, 'water_park/message.html', {'error_message': 'Invalid Login.'})
	return render(request, 'water_park/login.html')

def favorite_wp(request, pk):
	park = get_object_or_404(Park_Details, pk=pk)
	print "park :",park
	try:
		if park.is_fav:
			park.is_fav = False
		else:
			park.is_fav = True
		park.save()
	except (KeyError, Park_Details.DoesNotExist):
		return JsonResponse({'success': False})
	else:
		return render(request,'water_park/detail.html',{'parkid':park})

def favorite(request, pk):
	park = get_object_or_404(Park_Details, pk=pk)
	print "park :",park
	try:
		if park.is_fav:
			park.is_fav = False
		else:
			park.is_fav = True
		park.save()
	except (KeyError, Park_Details.DoesNotExist):
		return JsonResponse({'success': False})
	else:
		return render(request,'water_park/index.html',{'wp_list':Park_Details.objects.order_by('park_name')})

class UserFormView(View):

	form_class=UserForm
	template_name='water_park/registration_form.html'


	#display blank form
	#for get request eg: add userform, add waterpark form
	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	#process form data
	#for post request eg: submitting the above forms
	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user= form.save(commit=False) #not yet saved in DB due to commit=False

			#cleaned (normalized) data
			username=form.cleaned_data['username']	#if username is email for logging in
			# username=form.cleaned_data['email']			#if username is email for logging in
			password=form.cleaned_data['password']
			user.set_password(password)
			# user.active=False  ###send confirmation mail for activating account
			user.save()


			#returns User objects if credentials are correct
			user= authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
				# if user.active:
					login(request,user)
					# request.user.username
					return redirect('water_park:index')
				else:
					return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_name')})
			else:
				return render(request, 'water_park/message.html', {'error_message': 'Invalid Login.'})

		return render(request,self.template_name,{'form':form})

class ImageCreate(CreateView):
	model=Images
	fields=['park','image_name','image_url']

class ImageUpdate(UpdateView):
	model=Images
	fields=['park','image_name','image_url']

class ImageDelete(DeleteView):
	model=Images
	success_url=reverse_lazy('water_park:detail',kwargs={'pk' : model.id})


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

@login_required(login_url='water_park:login_user')
def add_image(request,park_id):
	form=ImagesForm(request.POST or None,request.FILES or None)
	park=get_object_or_404(Park_Details, pk=park_id)
	if form.is_valid():
		wp_images=park.images_set.all()
		for x in wp_images:
			if x.image_name==form.cleaned_data.get("image_name"):
				context={'park':park,'form':form,'error_message':'You already added that image',}
				return render(request, 'water_park/add_image.html', context)
		image=form.save(commit=False)
		image.park=park
		image.image_url=request.FILES['image_url']
		image.save()
		return render(request,'water_park/detail.html',{'parkid':park})
	context={'park':park,'form':form,}
	return render(request,'water_park/add_image.html',context)

@login_required(login_url='water_park:login_superuser')
def delete_image(request, park_id, image_id):
	if request.user.is_admin:
		park = get_object_or_404(Park_Details, pk=park_id)
		image = Images.objects.get(pk=image_id)
		image.delete()
		return render(request, 'water_park/detail.html', {'parkid': park})
	else:
		return render(request, 'water_park/message.html', {'error_message': 'User must be Super-User to delete images'})

class ImageFormView(View):

	form_class=ImagesForm
	template_name='water_park/add_images_form.html'

	def get(self,request):
		# return JsonResponse({'success': False})
		pass
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		# return JsonResponse({'success': False})
		form=self.form_class(request.POST)

		if form.is_valid():
			user= form.save(commit=False) #not yet saved in DB due to commit=False

			#cleaned (normalized) data
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()


			#returns User objects if credentials are correct
			user= authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					# request.user.username
					return redirect('water_park:index')

		return render(request,self.template_name,{'form':form})

def sort_parks(request,sort_id):
	park = Park_Details.objects.all()
	print "park :",park
	print "sort_id :",sort_id
	print "type :",type(sort_id)
	if int(sort_id)==0:
		return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_name')})
	elif int(sort_id)==1:
		return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_name').reverse()})
	elif int(sort_id)==2:
		return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_price')})		
	elif int(sort_id)==3:
		return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_price').reverse()})
	else:
		return render(request, 'water_park/index.html', {'wp_list': Park_Details.objects.order_by('park_name')})
