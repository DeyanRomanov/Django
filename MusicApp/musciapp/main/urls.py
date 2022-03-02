from django.urls import path

from musciapp.main.views import profile_delete, profile_details, album_delete, album_edit, album_details, add_album, \
    home_page, profile_create

urlpatterns = [
    path('', home_page, name='home page'),
    path('profile/details/', profile_details, name='profile details page'),
    path('profile/delete/', profile_delete, name='delete profile page'),
    path('profile/create/', profile_create, name='create profile page'),

    path('album/add/', add_album, name='add album page'),
    path('album/details/<int:pk>', album_details, name='album details page'),
    path('album/edit/<int:pk>/', album_edit, name='edit album page'),
    path('album/delete/<int:pk>', album_delete, name='delete album page'),
]
