from django.urls import path

from Petstagram.main.views import home, photo_details, dashboard, profile, like_photo, unauthorized, create_profile, \
    add_pet, pet_edit, pet_delete, add_photo, photo_edit, profile_edit, profile_delete

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('photo/details/<int:pk>/', photo_details, name='photo'),
    path('photo/like/<int:pk>/', like_photo, name='likes photo'),
    path('401/', unauthorized, name='401'),
    path('profile/create/', create_profile, name='create profile'),
    path('pet/add/', add_pet, name='add pet'),
    path('pet/edit/<int:pk>', pet_edit, name='edit pet'),
    path('pet/delete/<int:pk>', pet_delete, name='delete pet'),
    path('photo/add', add_photo, name='add photo'),
    path('photo/edit/<int:pk>', photo_edit, name='photo edit'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
]
