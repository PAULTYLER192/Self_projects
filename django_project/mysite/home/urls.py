from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns=[
  path('', views.home_view, name='home'),
  path('about/', views.about_view, name='about'),
  path('contact/', views.contact_view, name='contact'),
  path('blog/', PostListView.as_view(), name='post-list'),
  path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  ]
  