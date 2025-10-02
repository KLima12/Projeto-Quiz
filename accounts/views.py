from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from rest_framework_simplejwt.tokens import RefreshToken
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.urls import reverse


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            auth_login(self.request, user)

            refresh = RefreshToken.for_user(user)
            acess_token = str(refresh.access_token)
            refresh_token = str(refresh)

            next_url = self.request.GET.get(
                'next') or self.request.POST.get('next')

            sucess_url = self.get_success_url()

            if next_url:
                sucess_url = next_url

            query_string = urlencode({
                'acess_token': acess_token,
                'refresh_token': refresh_token
            })

            return redirect(f"{sucess_url}?{query_string}")

        def get_sucess_url(self):
            next_url = self.request.GET.get('next') or self.request.POST
            if next_url and is_safe_url(next_url, allowed_hosts=self.request.get_host()):
                return next_url

            return reverse('home')
