from django.urls import path
from .views import register, profile, CustomLoginView, home,logoutView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('', home , name='home'),


    #path('login', LoginView.as_view(template_name='login.html'), name='login'),
    #path('profile/', profile, name='profile'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    #path('register/', CustomRegisterView.as_view(), name='register'),
]




