
from django.contrib import admin
from django.urls import path, include
from .views import PostDetail, PostList, PostListDetailFilter

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('custom/', PostListDetailFilter.as_view(), name="post_filter")

]