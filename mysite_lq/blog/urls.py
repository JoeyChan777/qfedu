from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name='blog_titile'),
    url(r'(?P<article_id>\d)/$',views.blog_content,name='blog_content')
]