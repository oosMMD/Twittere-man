from django.shortcuts import render
from users.models import Follow
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/users/login')
def HomePage(request):
    me = Follow.objects.get(follower_slug=request.user)
    followings = me.other_guy.all
    # return HttpResponse(followings)
    posts = Post.objects.all()
    return render(request, 'home.html', {'followings': followings, 'posts': posts})
