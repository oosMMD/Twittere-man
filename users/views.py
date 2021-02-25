from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from posts.models import Post
from .models import Profile, Follow
from .forms import CreateProfile, Follow_form
from django.http import HttpResponse


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
        form3 = Follow_form(request.POST)
        if form.is_valid():
            user = form.save()
            instance = form2.save(commit=False)
            instance2 = form3.save(commit=False)
            instance.name = str(user.username)
            instance.user_slug = str(instance.name).strip()
            instance.save()
            instance2.me = user
            instance2.follower_slug = str(instance2.me).strip()
            instance2.save()
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


def follow_view(request, slug):
    other_user = Follow.objects.get(follower_slug=slug)  # in esme kasi ke gharare folow she ro barmigardoone(following)
    me = Follow.objects.get(follower_slug=request.user)  # in esme hesabe ma ro barmigardoone (follower)
    if me.me != other_user.me:
        if me.other_guy.filter(me=other_user).exists():
            me.other_guy.remove(other_user.me)
            return redirect('users:profile', slug=slug)
        else:
            me.other_guy.add(other_user.me)
            return redirect('users:profile', slug=slug)

    return redirect('users:profile', slug=slug)
