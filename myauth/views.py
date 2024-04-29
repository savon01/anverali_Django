from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import Profile
from .forms import ProfileForm


def home(request):
    return render(request, 'myauth/home.html')


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('myauth:home'))


class AboutMeView(LoginRequiredMixin, TemplateView):
    template_name = 'myauth/about-me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = user.profile
        context['profile'] = profile
        return context


@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('myauth:home')


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('myauth:about-me')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'myauth/edit-profile.html', context)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Создание профиля
        user = form.save()
        profile = Profile.objects.create(user=user)
        profile.is_customer = self.request.POST.get('is_customer') == 'on'
        profile.contact_info = self.request.POST.get('contact_info')
        profile.experience = self.request.POST.get('experience')
        profile.save()

        # Аутентификация и вход в систему
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)

        return response
