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
def update_post(request, id):
    try:
        post = Post.objects.get(id=id)  # ✅ FIXED
    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = PostSerializer(
        post,
        data=request.data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    post.delete()
    return Response({"message": "Post deleted successfully"}, status=204)
@api_view(['GET'])
def get_single_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = PostSerializer(post)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )