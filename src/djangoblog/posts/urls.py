from django.conf.urls import url

from . import views #relative import to post views


urlpatterns = [
	 
	url(r'^create/$',views.posts_create, name='create'),
	url(r'(?P<pk>\d+)/$',views.posts_detail, name='detail'), # takes an object id argument
	url(r'(?P<pk>\d+)/edit/$',views.posts_update, name='update'),
	url(r'(?P<pk>\d+)/delete/$',views.posts_delete, name='delete'),
	url(r'^$',views.posts_list, name='list' ), #list all posts kept last to ensure other views are seen first
]