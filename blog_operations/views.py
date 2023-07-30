from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import BlogModel
from rest_framework.permissions import IsAuthenticated
from .serializers import ShowBlogSerializer, AddBlogSerializer, ShowBlogDetailsSerializer, PutBlogSerializer, PatchBlogSerializer

# todo
#link foreign key with user and their post 

class ShowBlogView(APIView):
    def get(self, request):
        try:
            blogs = BlogModel.objects.all()
            serializer = ShowBlogSerializer(blogs, many=True)
            return Response({
                'blogs': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'No blogs found.', 'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


class AddBlogView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = AddBlogSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'blog': serializer.data,
                    'message': 'Blogs saved successfully!',
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Something went wrong! Unable to add blog.'
            }, status=status.HTTP_400_BAD_REQUEST)


class ShowBlogDetailsView(APIView):  # show single blog
    def get(self, request, pk):
        try:
            get_single_blog = BlogModel.objects.get(id=pk)
            serializer = ShowBlogDetailsSerializer(get_single_blog)
            return Response({'blog_detail': serializer.data}, status=status.HTTP_200_OK)
        except BlogModel.DoesNotExist:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)


class DeleteBlogView(APIView):
    def delete(self, request, pk):
        try:
            blog = BlogModel.objects.get(id=pk)
            blog.delete()
            return Response({'message': 'Selected blog deleted.'}, status=status.HTTP_200_OK)
        except BlogModel.DoesNotExist:
            return Response({'message': 'Blog not found!'}, status=status.HTTP_404_NOT_FOUND)


class PutBlogView(APIView):
    def put(self, request, pk):
        try:
            blog = BlogModel.objects.get(id=pk)
            data = request.data
            serializer = PutBlogSerializer(blog, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': 'Blog updated successfully1'}, status=status.HTTP_200_OK)
        except BlogModel.DoesNotExist:
            return Response({'message': 'Blog not found to be updated!'}, status=status.HTTP_404_NOT_FOUND)


class PatchBlogView(APIView):
    def patch(self, request, pk):
        try:
            blog = BlogModel.objects.get(id=pk)
            data = request.data
            serializer = PatchBlogSerializer(blog, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': 'Blog updated successfully using patch method!'}, status=status.HTTP_200_OK)
        except BlogModel.DoesNotExist:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
