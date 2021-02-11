from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.postspage, name='home'),
    path('create', views.create_post, name='create'),
    path('<slug>', views.post_detail, name='post_detail'),
]
