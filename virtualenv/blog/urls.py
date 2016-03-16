from django.conf.urls import url
from . import views #import blog/views.py

urlpatterns = [
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),# Django will take everything that you place here and transfer it to a view as a variable called pk. 
    url(r'^$', views.post_list, name='post_list'), # an empty string will match because http://127.0.0.1:8000/ is not a part of URL.
] # This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
  # name='post_list' is the name of the URL that will be used to identify the view.