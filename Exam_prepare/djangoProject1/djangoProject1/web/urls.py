from django.urls import path

from djangoProject1.web.views import show_home_page, show_create_expense, show_edit_expense, show_delete_expense, \
    show_profile, show_edit_profile, show_delete_profile, show_create_profile

urlpatterns = (
    path('', show_home_page, name='home'),
    path('create/', show_create_expense, name='create expense'),
    path('edit/<int:pk>', show_edit_expense, name='edit expense'),
    path('delete/<int:pk>', show_delete_expense, name='delete expense'),
    path('profile/', show_profile, name='profile'),
    path('profile/edit/', show_edit_profile, name='edit profile'),
    path('profile/delete/', show_delete_profile, name='delete profile'),
    path('profile/create/', show_create_profile, name='create profile'),
)
