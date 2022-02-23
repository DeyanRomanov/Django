from django.shortcuts import render, redirect

from Petstagram.main.forms import CreateProfile, CreatePet
from Petstagram.main.models import Profile, PetsPhoto, Pet
from Petstagram.main.templatetags.profiles import has_profile


def home(request):
    add_pets = True
    context = {
        'add_pets': add_pets,
    }
    return render(request, 'home_page.html', context)


def dashboard(request):
    if not has_profile():
        return redirect('401')
    pets = PetsPhoto.objects.prefetch_related('tagged_pets__user_profile')
    context = {
        'pets': pets,
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    if not has_profile():
        return redirect('401')
    profiles = Profile.objects.all()
    profiles = profiles[0]
    picture_upload = PetsPhoto.objects.prefetch_related('tagged_pets__user_profile').count()
    likes = PetsPhoto.objects.prefetch_related('tagged_pets__petsphoto_set').all()
    likes = sum([like.likes for like in likes])
    pets = Pet.objects.prefetch_related('user_profile__pet_set').all()
    context = {
        'likes': likes,
        'profiles': profiles,
        'picture_upload': picture_upload,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def photo_details(request, pk):
    if not has_profile():
        return redirect('401')
    photo = PetsPhoto.objects.get(pk=pk)
    context = {
        'photo': photo,
    }
    return render(request, 'photo_details.html', context)


def like_photo(request, pk):
    photo = PetsPhoto.objects.get(pk=pk)
    photo.likes += 1
    photo.save()
    return redirect('photo', pk)


def unauthorized(request):
    return render(request, '401.html')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateProfile()
    context = {
        'form': form
    }
    return render(request, 'profile_create.html', context)


def add_pet(request):
    if request.method == 'POST':
        form = CreatePet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = CreatePet()
    context = {
        'form': form,
    }
    return render(request, 'pet_create.html', context)


def pet_edit(request, pk):
    return render(request, )


def pet_delete(request, pk):
    return render(request, )


def add_photo(request):
    return render(request, )


def photo_edit(request, pk):
    return render(request, )


def profile_edit(request):
    return render(request, )


def profile_delete(request):
    return render(request, )
