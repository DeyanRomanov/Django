from django.contrib.auth import views
from django.urls import reverse_lazy

from common.view_mixins import RedirectToDashboard


class UserRegisterView(RedirectToDashboard):
    pass


class UserLoginView(views.LoginView):
    template_name = 'login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailsView:
    pass


class UserEditView:
    pass


class UserChangePasswordView:
    pass
