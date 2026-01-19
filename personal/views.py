from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
@api_view(['GET'])
def get_data(request):
    posts = Post.objects.all()
    if not posts.exists():
        return Response({
            "message": "No blog posts available",
            "data": []
        })
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def add_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    serializer = PostSerializer(
        post,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    post.delete()
    return Response({"message": "Post deleted successfully"}, status=204)
@api_view(['GET'])
def get_single_post(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)
    return Response(post.data, status=204)