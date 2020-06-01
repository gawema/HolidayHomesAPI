from django.urls import path

from . import views

urlpatterns = [
    path('houses/', views.HouseList.as_view()),
    path('houses/<int:pk>/', views.HouseDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('profile/', views.OwnProfile.as_view()),
    path('profile/houses/', views.OwnHouseList.as_view()),

    path('bookings/', views.BookingList.as_view()),
    path('bookings/<int:pk>/', views.BookingDetail.as_view()),

    path('facilities/', views.FacilityList.as_view()),
    path('facilities/<int:pk>/', views.FacilityDetail.as_view()),

    path('housefacilities/', views.HouseFacilityList.as_view()),
    path('housefacilities/<int:pk>/', views.HouseFacilityDetail.as_view()),

    path('gallery/', views.GalleryList.as_view()),
    path('gallery/<int:pk>/', views.GalleryDetail.as_view()),

    path('ig/posts/', views.getIgPost),

]

