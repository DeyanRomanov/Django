from django.urls import path

from Petstagram.Web.views import show_home_page, show_profile_details, show_photo_details, show_dashboard, like_photo

urlpatterns = (
    path('', show_home_page, name='home'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('photo/details/photo<int:pk>', show_photo_details, name='photo_details'),
    path('profile/', show_profile_details, name='profile_details'),
    path('photo/like/<int:pk>/', like_photo, name='like button'),
)
