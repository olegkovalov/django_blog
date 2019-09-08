from django.urls import path

from .views import blog_views

urlpatterns = [
    path('posts/', blog_views.PostListCreateAPIView.as_view(), name='api-post-list'),
    path('posts/<uuid:pk>/', blog_views.PostDetailsAPIView.as_view(), name='api-post-details'),
]
