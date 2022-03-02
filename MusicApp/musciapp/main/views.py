from django.shortcuts import render, redirect

from musciapp.main.forms import CreateProfile, DeleteProfile, AddAlbum, EditAlbum, DeleteAlbum
from musciapp.main.models import Album
from musciapp.main.templatetags.has_profile import has_profile


def home_page(request):
    albums = Album.objects.all()
    profile = has_profile()
    context = {
        'albums': albums,
    }
    if not profile:
        return redirect('create profile page')
    return render(request, 'home-with-profile.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = CreateProfile()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = has_profile()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = has_profile()
    album_to_delete = Album.objects.all()
    if request.method == 'POST':
        form = DeleteProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            album_to_delete.delete()
            return redirect('home page')
    return render(request, 'profile-delete.html')


def add_album(request):
    if request.method == 'POST':
        form = AddAlbum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = AddAlbum()
    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = EditAlbum(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album_to_delete = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbum(request.POST, instance=album_to_delete)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = DeleteAlbum(instance=album_to_delete)
    context = {
        'form': form,
        'album_to_delete': album_to_delete,
    }
    return render(request, 'delete-album.html', context)
