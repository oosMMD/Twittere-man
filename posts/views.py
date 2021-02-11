from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth.decorators import login_required


def postspage(request):
    posts = models.Post.objects.all()
    return render(request, 'posts_page.html', {'posts': posts})


def post_detail(request, slug):
    post = models.Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})


@login_required(login_url='/users/login')
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        instance = form.save(commit=False)
        instance.author = request.user
        instance.slug = instance.title.strip()
        instance.save()
        return redirect('posts:home')
    form = forms.CreatePost
    return render(request, 'create_post.html', {'form': form})
