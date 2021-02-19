from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.users, name='users'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('<slug>', views.profile, name='profile')
]
