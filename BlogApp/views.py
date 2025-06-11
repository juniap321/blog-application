from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse

class PostPagination(PageNumberPagination):
    page_size = 5

class CommentPagination(PageNumberPagination):
    page_size = 3

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

@method_decorator(csrf_protect, name='dispatch')
class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('post-list')


class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post-list')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

class PostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        paginator = PostPagination()
        result = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return redirect('post-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return render(request, 'post_detail.html', {'post': serializer.data})

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post.author != request.user:
            return Response({'error': 'You can only delete your own posts.'}, status=403)
        post.delete()
        return redirect('post-list')

class CommentCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, author=request.user)
            return redirect('post-detail', pk=post_id)
        return Response(serializer.errors, status=400)
