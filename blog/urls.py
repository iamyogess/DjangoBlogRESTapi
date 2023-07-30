from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('accounts.urls')),
    path('api/main/', include('blog_operations.urls')),
]
