from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='home'),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
]
