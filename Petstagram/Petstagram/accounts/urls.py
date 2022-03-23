from django.urls import path

from Petstagram.accounts.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    # path('create-profile/',,name='create profile'),
    # path('profile/<int:pk>/',,name='details profile'),
    # path('edit-profile/<int:pk>/',,name='edit profile'),
    # path('edit-password/<int:pk>/',,name='edit password'),
]
