from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views


urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token, name='api-toke-auth'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
