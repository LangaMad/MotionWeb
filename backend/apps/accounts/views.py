from django.shortcuts import render,redirect
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
    UpdateView)
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from .models import User

from .forms import LoginForm,UserRegisterForm

from django.urls import reverse_lazy


# Create your views here.
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username  = data['username']
        email = data['email']
        password = data['password']
        user = authenticate(username=username,email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponseRedirect(reverse('error'))
        return HttpResponseRedirect(reverse('error'))

class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')


def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')