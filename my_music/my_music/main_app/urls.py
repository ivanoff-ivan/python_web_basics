from django.urls import path

from my_music.main_app.views import show_home_page, show_album_add_page, show_album_details_page, show_album_edit_page, \
    show_album_delete_page, show_profile_details_page, show_profile_delete_page

urlpatterns = [
    path('', show_home_page, name='home page'),
    path('album/add/', show_album_add_page, name='add album page'),
    path('album/details/<int:pk>/', show_album_details_page, name='album details page'),
    path('album/edit/<int:pk>/', show_album_edit_page, name='edit album page'),
    path('album/delete/<int:pk>/', show_album_delete_page, name='delete album page'),
    path('profile/details/', show_profile_details_page, name='profile details page'),
    path('profile/delete/', show_profile_delete_page, name='delete profile page'),
]
