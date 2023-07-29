from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserPasswordChangeSerializer, SendPasswordResetEmailSerializer

# Generate Token


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


# User Registrations View
class UserRegistrationView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserRegistrationSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                token = get_token_for_user(user)
                return Response({
                    'message': 'Registration Successful!',
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Registration Failed!', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserLoginSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                user = authenticate(email=email, password=password)
                if user is not None:
                    token = get_token_for_user(user)
                    return Response({
                        'token': token,
                        'message': 'Login Successful!'
                    }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Login Failed! Wrong Credentials',
                'error': str(e)
            }, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserPasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            user = request.user
            serializer = UserPasswordChangeSerializer(
                data=data, context={'user': user})
            if serializer.is_valid(raise_exception=True):
                return Response({
                    'message': 'Password Changed Successfully1'
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e),
                'message': 'Something went wrong!'
            }, status=status.HTTP_400_BAD_REQUEST)


class SendResetPasswordEmailView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = SendPasswordResetEmailSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                return ({'message': 'Password Reset Email Sent. Please check your email.'})
        except Exception as e:
            return Response({'message': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)
