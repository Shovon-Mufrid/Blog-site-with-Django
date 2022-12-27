from django.urls import path
from . import views

app_name = 'Login_App'


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.sign_in, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('change/', views.user_change, name='change'),
    path('pass_change/', views.pass_change, name='pass_change'),
]

