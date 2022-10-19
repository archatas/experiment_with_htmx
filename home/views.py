from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django_htmx.http import HttpResponseClientRefresh
from .forms import SearchForm, LoginForm


def home(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    if request.GET:
        form = SearchForm(data=request.GET, prefix="search")
        if form.is_valid():
            pass
    else:
        form = SearchForm(data=request.GET, prefix="search")
    request.combined_media = form.media
    context = {
        "form": form,
    }
    return render(request, "home.html", context)


def login(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST, prefix="login")
        template_name = "login_form.html"
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return HttpResponseClientRefresh()
    else:
        form = LoginForm(request=request, prefix="login")
        template_name = "login_dialog.html"
    context = {"form": form}
    return render(request, template_name, context)


def logout(request):
    auth_logout(request)
    return redirect("home")
