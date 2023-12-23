from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.
from django.urls import reverse_lazy
from django.contrib import messages
from . forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.views.generic import CreateView,FormView
from django.contrib.auth.views import LoginView,LogoutView

# def musician(request):
#     if request.method=='POST':
#         music_form = forms.MusicianForm(request.POST)
#         if music_form.is_valid():
#             messages.success(request, 'Successfully added a musician')
#             music_form.save()
#             return redirect('musician_page')
#     else:
#         music_form=forms.MusicianForm()
#         return render(request, 'musicians.html', {'form': music_form})

    
#class based view musician
@method_decorator(login_required, name = 'dispatch')
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musicians.html'
    success_url = reverse_lazy('musician_page')
    def form_valid(self, form):
        messages.success(self.request, 'Successfully added a musician')
        return super().form_valid(form)
        

# def registration(request):
#     if not request.user.is_authenticated:
#         if request.method == 'post':
#             regis_form = RegistrationForm(request.POST)
#             if regis_form.is_valid():
#                 messages.success(request, 'Account create successfully')
#                 regis_form.save()
#         else:
#             regis_form = RegistrationForm()
#             return render(request,'registration.html', {'form':regis_form})
#     else:
#         return redirect('home_page')
    
    
#class based view Registration 
class RegistrationCreateView(FormView):
    form_class = forms.RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login_page')

    def form_valid(self,form):
        if not self.request.user.is_authenticated:
            messages.success(self.request, 'Account create successfully')
            form.save()
            return super().form_valid(form)
        return redirect('login_page')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('login_page')

    
# def log_in(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             log_form = AuthenticationForm(request=request, data=request.POST)
#             if log_form.is_valid():
#                 messages.success(request, 'Logged in successfully')
#                 name = request.cleaned_data['username']
#                 pass_word = request.cleaned_data['password']
#                 user = authenticate(username=name, password=pass_word)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('musician_page')
#         else:
#             log_form=AuthenticationForm() 
#             return render(request,'login.html', {'form': log_form})
#     else:
#         return redirect('registration_page')


#class based view login
class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('musician_page')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            user = authenticate(username = name, password = pass_word)
            if user is not None:
                login(self.request, user)
                messages.success(self.request, 'Logged in successfully')
                return redirect('album_showing_page')
        else:
            return redirect('registration_page')
        
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('registration_page')
        

@method_decorator(login_required , name = 'dispatch')
class UserLogoutView(LogoutView):
    def get(self,request):
        logout(request)
        messages.success(self.request, 'Logout successfully')
        return redirect('home_page')
    