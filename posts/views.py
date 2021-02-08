from django.shortcuts import render


def postspage(request):
    return render(request, 'posts_page.html')
