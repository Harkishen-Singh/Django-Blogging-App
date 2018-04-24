from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='homepage'),
    path('post', views.BlogListView.as_view(), name='allPosts'),
    path('post/<int:pk>', views.BlogDetailedView.as_view(), name='detailedBlog'),
]
