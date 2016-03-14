from django.conf.urls import url
from . import views #import blog/views.py

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # an empty string will match because http://127.0.0.1:8000/ is not a part of URL.
] # This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
  # name='post_list' is the name of the URL that will be used to identify the view.