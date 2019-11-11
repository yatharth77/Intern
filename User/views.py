from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm

from .models import Profile
def login_view(request):
    if request.user.is_authenticated():
        return redirect("../loggedIn")

    title = "Login"

    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        profile_obj = Profile.objects.get(user=request.user)
        user_type=profile_obj.user_type

        return redirect("../loggedIn")
    return render(request, "form.html", {"form":form,"title": title,"flag":1})


def register_view(request):
    if request.user.is_authenticated():
        return redirect("../loggedIn")
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None, request.FILES or None)

    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save();

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("../loggedIn")

    context = {
        "form": form,
        "profile_form": profile_form,
        "title": title,
        "flag":2,
    }
    return render(request, "form.html", context)

@login_required
def logout_view(request):
    logout(request)
    return redirect("../login")

@login_required
def home_view(request):
    profile_obj = Profile.objects.get(user=request.user)
    user_type=profile_obj.user_type
    if user_type=="Dealer":
        return render(request, "dash1.html", {"user": request.user,"profile": profile_obj})
    else:
        return render(request, "dash2.html", {"user": request.user,"profile": profile_obj})

def index_view(request):
    return render(request, "index.html", {})
