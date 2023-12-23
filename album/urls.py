from django.urls import path
from . import views
urlpatterns = [
    # path('add/', views.music_album, name='album_page'),

    path('add/', views.MusicAlbum.as_view(), name='album_page'),
    path('adds/', views.Musics_album, name='album_showing_page'),
    path('edit/<int:id>', views.EditAlbumView.as_view(), name='edit_page'),
    path('delete/<int:id>', views.deleteView.as_view(), name='delete_page'),
]
