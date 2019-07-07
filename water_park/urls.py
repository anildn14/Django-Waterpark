from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name="water_park"

urlpatterns = [
	url(r'^$',views.index,name='index'),

	url(r'^register/$',views.UserFormView.as_view(),name='register'),

	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^login_superuser/$', views.login_superuser, name='login_superuser'), #purposely kept url as login_user as the user should not know whether superuser is called or normal user
	url(r'^logout_user/$', views.logout_user, name='logout_user'),

	url(r'^(?P<park_id>[0-9]+)/add_image/$',views.add_image,name='add_image'),

	url(r'^(?P<park_id>[0-9]+)/delete_image/(?P<image_id>[0-9]+)$',views.delete_image,name='delete_image'),

	# /waterparks/14 --->(some_id)
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),

	# /waterparks/<wp_id>/favorite
	url(r'^(?P<pk>[0-9]+)/favorite_wp/$', views.favorite_wp, name='favorite_park'),

	url(r'^(?P<pk>[0-9]+)/favorite_park/$', views.favorite, name='favorite_indexpg'),

	# /waterparks/wp/add/
	url(r'^wp/add/$',views.create_waterpark,name='wp-add'),

	# /waterparks/wp/2<wp_id>/update/
	url(r'^wp/(?P<pk>[0-9]+)/update/$',views.WaterParkUpdate.as_view(),name='wp-update'),

	# /waterparks/wp/2<wp_id>/delete
	url(r'^wp/(?P<park_id>[0-9]+)/delete/$',views.delete_waterpark,name='wp-delete'),

	url(r'^comments/$',views.comments,name='comments'),
	url(r'^add-comment/$',views.add_comment,name='add-comment'),
	url(r'^(?P<com_id>[0-9]+)/comment-delete/$',views.delete_comment,name='delete-comment'),
	url(r'^(?P<sort_id>[0-9]+)/sort-parks/$',views.sort_parks,name='sort-parks'),
]	
