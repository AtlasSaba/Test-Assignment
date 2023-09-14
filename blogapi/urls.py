from django.urls import include, path
from . import views


urlpatterns = [
    path('all-posts/', views.ListAllPosts.as_view()),
    path('blog-post/<int:pk>/', views.BlogPostView.as_view()),

]