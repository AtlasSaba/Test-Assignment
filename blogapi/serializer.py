from rest_framework import serializers
from .models import BlogPost


class AllPostsSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogPost
		# fields = '__all__'
		exclude = ['author']



# class CreateBlogPostSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = BlogPost
# 		fields = '__all__'