from django.shortcuts import render, redirect

from Petstagram.Web.models import Profile, PetsPhoto, Pet


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home_page(request):
    profile = get_profile()
    context = {
        'hide_navi_bar': profile,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pets_photos = set(PetsPhoto.objects.prefetch_related('tagged').filter(tagged__user_profile=profile))
    context = {
        'pets_photos': pets_photos
    }
    return render(request, 'dashboard.html', context)


def show_photo_details(request, pk):
    photo_details = PetsPhoto.objects.prefetch_related('tagged').get(pk=pk)
    context = {
        'photo_details': photo_details,
    }
    return render(request, 'photo_details.html', context)


def show_profile_details(request):
    profile = Profile.objects.get()
    all_pet = Pet.objects.prefetch_related('user_profile__pet_set').all()
    context = {
        'profile': profile,
        'all_pet': all_pet,
    }
    return render(request, 'profile_details.html', context)


def like_photo(request, pk):
    photo = PetsPhoto.objects.prefetch_related('tagged').get(pk=pk)
    photo.likes += 1
    photo.save()

    return redirect('photo_details', pk)
