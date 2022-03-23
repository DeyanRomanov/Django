from django.urls import path

from Recipes.main.views import home_view, create_view, edit_view, delete_view, details_view

urlpatterns = (
    path('', home_view, name='home'),
    path('create/', create_view, name='create'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('delete/<int:pk>', delete_view, name='delete'),
    path('details/<int:pk>', details_view, name='details'),
)
