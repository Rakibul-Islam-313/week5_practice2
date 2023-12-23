from django.urls import path 
from .import views
urlpatterns = [
    # path('add/',views.musician, name='musician_page'),
    # path('register/',views.registration, name='registration_page'),
    # path('login/',views.log_in, name='login_page'),
    path('add/',views.AddMusicianCreateView.as_view(), name='musician_page'),
    path('register/',views.RegistrationCreateView.as_view(), name='registration_page'),
    path('login/',views.UserLoginView.as_view(), name='login_page'),
    path('logout/',views.UserLogoutView.as_view(), name='logout_page'),
]
