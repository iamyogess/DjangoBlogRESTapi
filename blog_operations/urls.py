from django.urls import path
from .views import ShowBlogView, AddBlogView, ShowBlogDetailsView, DeleteBlogView, PutBlogView, PatchBlogView


urlpatterns = [
    path('blogs/', ShowBlogView.as_view(), name='blogs'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('blog_details/<str:pk>/',
         ShowBlogDetailsView.as_view(), name='blog_details'),
    path('delete_blog/<str:pk>/', DeleteBlogView.as_view(), name='delete_blog'),
    path('put_blog/<str:pk>/', PutBlogView.as_view(), name='put_blog'),
    path('patch_blog/<str:pk>/', PatchBlogView.as_view(), name='patch_blog'),
]
