from django.contrib.auth.views import PasswordResetView
from django.urls import path
from .views import ProfileView
from .views import login_view, logout_view
from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('profile/', ProfileView, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),

    path('profile/', ProfileView, name='profile')

]
