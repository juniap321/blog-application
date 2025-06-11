from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post-list'),
    path('create/', PostListCreateAPIView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('post/<int:post_id>/comment/', CommentCreateAPIView.as_view(), name='add-comment'),
    path('register/', RegisterView.as_view(), name='register'),  
     path('login/', LoginView.as_view(), name='login'),
     
    
]
