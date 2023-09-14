from .models import BlogPost
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AllPostsSerializer
from rest_framework.permissions import IsAuthenticated
from .authentication import (
    IsAuthenticatedExceptGet,
    IsPostAuthor
)
from rest_framework import status


class ListAllPosts(APIView):
    permission_classes = [IsAuthenticatedExceptGet]

    def get(self, request):
        posts = BlogPost.objects.all()
        serializer = AllPostsSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AllPostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class BlogPostView(APIView):
    permission_classes = [IsAuthenticatedExceptGet, IsPostAuthor]

    def get(self, request, pk):
        try:
            posts = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"message": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AllPostsSerializer(posts)
        return Response(serializer.data)


    def put(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"message": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AllPostsSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    def delete(self, request, pk):
            try:
                blog_post = BlogPost.objects.get(pk=pk)
            except BlogPost.DoesNotExist:
                return Response({"message": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)
            blog_post.delete()
            return Response({"message": "successfully deleted blog post"})


