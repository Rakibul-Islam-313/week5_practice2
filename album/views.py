from typing import Any
from django.shortcuts import render
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
# from django.shortcuts import render,redirect
from .import forms 
from . import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from album.models import Album
# Create your views here.

def Musics_album(request):
    result = Album.objects.all()
    return render(request, 'album_showing.html', {'result':result})

# def music_album(request):
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('album_page')
#     else:
#         album_form=forms.AlbumForm()
#         return render(request,'albums.html',{'form':album_form})
    
# class based view
@method_decorator(login_required, name = 'dispatch')
class MusicAlbum(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'albums.html'
    success_url = reverse_lazy('album_page')

    def form_valid(self, form):
        messages.success(self.request, 'Add Album Successfully')
        return super().form_valid(form)

# class based view 
@method_decorator(login_required, name = 'dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'albums.html'
    success_url = reverse_lazy('album_page')

    def get_object(self):
        id = self.kwargs.get('id')
        return models.Album.objects.get(pk=id)

    def form_valid(self, form):
        return super().form_valid(form)
    
#class based View
@method_decorator(login_required, name = 'dispatch')
class deleteView(DeleteView):
    model = models.Album
    success_url = reverse_lazy('album_page')

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return models.Album.objects.get(pk = id)
        

