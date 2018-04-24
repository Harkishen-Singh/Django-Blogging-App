from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='homepage'),
    path('post', views.BlogListView.as_view(), name='allPosts'),
    path('post/<int:pk>', views.BlogDetailedView.as_view(), name='detailedBlog'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new',)
]
