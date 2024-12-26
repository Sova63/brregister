from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse_lazy,reverse
from django.contrib.auth import get_user_model, authenticate,login,logout
from django.views.generic import FormView, RedirectView
from .forms import LoginForm


class CustomLoginView(FormView):
    template_name = 'myregister/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myregister/register.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        message = f"Добро пожаловать, {request.user.username}!"
    else:
        message = "Добро пожаловать, гость!"
    return render(request, 'myregister/home.html', {'message': message})


@login_required
def profile(request):
    return render(request, 'myregister/profile.html', {'user': request.user})



class logoutView(RedirectView):
    def get_redirect_url(self, *args,**kwargs):
        logout(self.request)
        return reverse('home')


'''class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        # Дополнительная логика перед входом пользователя
        response = super().form_valid(form)
        print(f"Пользователь {self.request.user.username} вошел в систему.")
        return response


class CustomRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Дополнительная логика после регистрации пользователя
            print("Новый пользователь зарегистрирован.")
            return redirect('login')
        return render(request, 'register.html', {'form': form})'''





