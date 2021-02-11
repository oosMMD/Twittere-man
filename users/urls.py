from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.users, name='users'),
    path('profile/<str:user_name>', views.profile, name='profile'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    path('follow/<str:user_name>', views.follow_user, name='follow'),
    path('logout', views.logout_view, name='logout')
]
