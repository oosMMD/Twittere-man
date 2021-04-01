from django.shortcuts import render
from users.models import Follow, Profile
from posts.models import Post
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login')
def HomePage(request):
    me = Follow.objects.get(follower_slug=request.user)
    my_name = Profile.objects.get(name=request.user)
    followings = me.other_guy.all
    posts = Post.objects.all()
    return render(request, 'home.html', {'followings': followings, 'posts': posts, 'my_name': my_name})
