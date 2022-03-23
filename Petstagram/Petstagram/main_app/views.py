from django.urls import reverse_lazy
from django.views import generic

from Petstagram.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from Petstagram.accounts.models import Profile
from Petstagram.main_app.forms import AddPetForm
from Petstagram.main_app.models import PetPhoto, Pet
from common.view_mixins import RedirectToDashboard


class IndexView(RedirectToDashboard, generic.TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_nav'] = True
        return context


class DashboardView(generic.ListView):
    template_name = 'dashboard.html'
    model = PetPhoto
    context_object_name = 'pets_photos'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    # if Pet.date_of_birth:
    #     context['age'] = AddPetForm.clean_date_of_birth
    # return context


# def dashboard(request):
#     if not has_profile():
#         return redirect('401')
#     pets = PetsPhoto.objects.prefetch_related('tagged_pets__user_profile')
#     context = {
#         'pets': pets,
#     }
#     return render(request, 'dashboard.html', context)


class DetailsProfileView(generic.DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_profile_id=self.object.user_id))
        pets_photo = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
        total_pet_photos_count = len(pets_photo)
        total_likes_count = sum(pet.likes for pet in pets_photo)

        context.update({
            'total_likes_count': total_likes_count,
            'total_pet_photo_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'pets': pets,
        })
        return context
# def profile_view(request):
#     return render(request, 'profile_details.html')


class CreateProfileView(generic.CreateView):
    form_class = CreateProfileForm
    template_name = 'profile_create.html'
    success_url = reverse_lazy('dashboard')


# def profile_create(request):
#     return render(request, 'profile_create.html')


class EditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile details')


# def profile_edit(request):
#     return render(request, 'profile_edit.html')


class DeleteProfileView(generic.DeleteView):
    form_class = DeleteProfileForm
    template_name = 'profile_delete.html'
    success_url = reverse_lazy('index')


# def profile_delete(request):
#     return render(request, 'profile_delete.html')


class DetailsPhotoView(generic.DetailView):
    template_name = 'photo_details.html'
    model = PetPhoto

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('tagged_pets')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context
# def photo_detail(request):


#     return render(request, 'photo_details.html')


class AddPhotoView(generic.CreateView):
    template_name = 'photo_create.html'
    success_url = reverse_lazy('dashboard')
    model = PetPhoto
    fields = ('photo', 'description', 'tagged_pets')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# def photo_add(request):
#     return render(request, 'photo_create.html')


class EditPhotoView(generic.UpdateView):
    template_name = 'photo_edit.html'
    success_url = reverse_lazy('photo detail')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


# def photo_edit(request):
#     return render(request, 'photo_edit.html')
class AddPetView(generic.CreateView):
    template_name = 'pet_create.html'
    success_url = reverse_lazy('dashboard')
    form_class = AddPetForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    #
    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #     return super().get_success_url()


# def pet_add(request):
#     return render(request, 'pet_create.html')


class EditPetView(generic.CreateView):
    template_name = 'pet_create.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


# def pet_edit(request):
#     return render(request, 'pet_edit.html')


class DeletePetView(generic.DeleteView):
    template_name = 'pet_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
# def pet_delete(request):
#     return render(request, 'pet_delete.html')
