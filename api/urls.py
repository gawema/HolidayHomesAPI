from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListHouse.as_view()),
    path('<int:pk>/', views.DetailHouse.as_view()),
]