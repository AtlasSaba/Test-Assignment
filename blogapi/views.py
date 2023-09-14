from .models import BlogPost
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AllPostsSerializer
from rest_framework.permissions import IsAuthenticated

class ListAllPosts(APIView):

	def get(self,request):
		posts =  BlogPost.objects.all()
		serializer = AllPostsSerializer(posts, many=True)
		return Response(serializer.data)

	# @permission_class([IsAuthenticated])
	def post(self,request):
		serializer = AllPostsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.validated_data['author'] = request.user
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)


class BlogPostView(APIView):

	authetication_classes = []
	permission_classes = []

	def get(self,request, pk):
		posts =  BlogPost.objects.get(pk=pk)
		serializer = AllPostsSerializer(posts)
		return Response(serializer.data)

	def put(self,request, pk):
		blog_post = BlogPost.objects.get(pk=pk)
		serializer = AllPostsSerializer(posts, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors)


	def delete(self,request, pk):
		blog_post = BlogPost.objects.get(pk=pk)
		blog_post.delete()
		return Response({"message":"successfully deleted blog post"})


