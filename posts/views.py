from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth.decorators import login_required
from users import models as m


@login_required(login_url='/users/login')
def postspage(request):
    posts = models.Post.objects.all()
    return render(request, 'posts_page.html', {'posts': posts})


@login_required(login_url='/users/login')
def post_detail(request, slug):
    post = models.Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})


@login_required(login_url='/users/login')
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        instance = form.save(commit=False)
        instance.author = request.user
        number = 1
        instance.slug = instance.title.strip()
        while models.Post.objects.filter(slug=instance.slug):
            instance.slug = instance.title.strip() + str(number)
            number += 1
        instance.auth_slug = str(instance.author).strip()
        instance.save()
        return redirect('posts:home')
    form = forms.CreatePost
    return render(request, 'create_post.html', {'form': form})


@login_required(login_url='/users/login')
def deletepost(request, slug):
    me = m.Profile.objects.get(name=request.user).name
    post = models.Post.objects.get(slug=slug)
    if post.author == me:
        post.delete()
    return redirect('posts:home')
