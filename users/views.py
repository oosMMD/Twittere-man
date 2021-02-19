from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from posts.models import Post
from .models import Profile
from .forms import CreateProfile


def users(request):
    return render(request, 'usersPage.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form2 = CreateProfile(request.POST)
        if form.is_valid():
            user = form.save()
            instance = form2.save(commit=False)
            instance.name = str(user.username)
            instance.user_slug = str(instance.name).strip()
            instance.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request, slug):
    posts = Post.objects.all()
    form = Profile.objects.get(user_slug=slug)
    return render(request, 'profile.html', {'form': form, 'posts': posts})
