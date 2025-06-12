from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post'),
    path('postdetails/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('commentcreate/<int:post_id>/comment/', CommentCreateAPIView.as_view(), name='add-comment'),
    path('register/', RegisterView.as_view(), name='register'),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     
    
]
