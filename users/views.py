from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Followers, User


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
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request, user_name):
    user_obj = User.objects.get(name=user_name)
    session_user = User.objects.get(name=request.session['user'])
    session_following, create = Followers.objects.get_or_create(user=session_user)
    following, create = Followers.objects.get_or_create(user=session_user.id)
    check_user_followers = Followers.objects.filter(another_user=user_obj)

    is_followed = False
    if session_following.another_user.filter(name=user_name).exists() or following.another_user.filter(
            name=user_name).exists():
        is_followed = True
    else:
        is_followed = False

    param = {'user_obj': user_obj, 'followers': check_user_followers, 'following': following,
             'is_followed': is_followed}
    if 'user' in request.session:
        return render(request, 'profile.html', param)
    else:
        return redirect('users:users')


def follow_user(request, user_name):
    other_user = User.objects.get(name=user_name)
    session_user = request.session['user']
    get_user = User.objects.get(name=session_user)
    check_follower = Followers.objects.get(user=get_user.id)
    is_followed = False
    if other_user.name != session_user:
        if check_follower.another_user.filter(name=other_user).exists():
            add_usr = Followers.objects.get(user=get_user)
            add_usr.another_user.remove(other_user)
            is_followed = False
            return redirect(f'/profile/{session_user}')
        else:
            add_usr = Followers.objects.get(user=get_user)
            add_usr.another_user.add(other_user)
            is_followed = True
            return redirect(f'/profile/{session_user}')

        return redirect(f'/profile/{session_user}')
    else:
        return redirect(f'/profile/{session_user}')
