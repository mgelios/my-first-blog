from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/post/drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^blog/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^blog/post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^blog/post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^blog/post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^blog/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^blog/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^blog/categories/$', views.category_list, name='category_list'),
    url(r'^blog/category/(?P<pk>\d+)/$', views.category_posts, name='category'),
]