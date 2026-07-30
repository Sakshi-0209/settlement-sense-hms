from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class UserLoginView(LoginView):

    template_name = "authentication/login.html"

    redirect_authenticated_user = True


def user_logout(request):

    logout(request)

    return redirect("login")