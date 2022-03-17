from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # slug keyword name matches the 'slug' parameter in the get method
    # of the PostDetail class in the blog/views.py file.
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]