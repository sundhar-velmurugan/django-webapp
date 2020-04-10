from django.urls import path
from . import views

urlpatterns = [
  # path('', views.home, name='blog-home'),
  path('', views.PostListView.as_view(), name='blog-home'),
  path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
  path('about/', views.about, name='blog-about')
]