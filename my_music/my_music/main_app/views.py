from django.shortcuts import render, redirect

from my_music.main_app.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteProfileForm, DeleteAlbumForm
from my_music.main_app.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home_page(request):
    profile = get_profile()
    if profile:
        albums = Album.objects.all()
        context = {
            'albums': albums,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == "POST":
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
        else:
            form = CreateProfileForm()

        context = {
            'form': form,
            'no_profile': True,
        }
        return render(request, 'home-no-profile.html', context)


def show_album_add_page(request):
    if request.method == "POST":
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AddAlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)



def show_album_details_page(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def show_album_edit_page(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def show_album_delete_page(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
    }
    return render(request, 'delete-album.html', context)


def show_profile_details_page(request):
    profile = get_profile()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums_count': len(albums),
    }

    return render(request, 'profile-details.html', context)


def show_profile_delete_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
