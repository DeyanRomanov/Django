from django.urls import path

from Petstagram.main_app.views import IndexView, DashboardView, DetailsProfileView, CreateProfileView, EditProfileView, \
    DeleteProfileView, AddPhotoView, EditPhotoView, AddPetView, EditPetView, DeletePetView, DetailsPhotoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('photo/details/<int:pk>/', DetailsPhotoView.as_view(), name='photo detail'),
    path('photo/add/', AddPhotoView.as_view(), name='photo add'),
    path('photo/edit/', EditPhotoView.as_view(), name='photo edit'),

    path('pet/add/', AddPetView.as_view(), name='pet add'),
    path('pet/edit/<int:pk>', EditPetView.as_view(), name='pet edit'),
    path('pet/delete/<int:pk>', DeletePetView.as_view, name='pet delete'),

    path('profile/<int:pk>', DetailsProfileView.as_view(), name='profile details'),
    path('profile/create/', CreateProfileView.as_view(), name='profile create'),
    path('profile/edit/', EditProfileView.as_view(), name='profile edit'),
    path('profile/delete/', DeleteProfileView.as_view(), name='profile delete'),
]
