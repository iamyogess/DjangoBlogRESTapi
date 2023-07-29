from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserPasswordChangeView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('user-profile/', UserProfileView.as_view(), name='user_profile'),
    path('password-change/', UserPasswordChangeView.as_view(),
         name='user_password_change'),
]
