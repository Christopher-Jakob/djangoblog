from django.conf.urls import url

from . import views #relative import to post views


urlpatterns = [
	url(r'^$',"views.posts_list" ), #list all posts
	url(r'create/^$',"views.posts_create" ),
	url(r'detail/^$',"views.posts_detail" ),
	url(r'update/^$',"views.posts_update" ),
	url(r'delete/^$',"views.posts_delete" ),

]