<<<<<<< HEAD
from django.contrib.auth.views import PasswordResetView
=======
<<<<<<< HEAD
from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('profile/', ProfileView, name='profile')
=======
>>>>>>> 14c692bad7bea83d50b6c2bbeef94fb1fc87fe22
from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
<<<<<<< HEAD
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),

=======
>>>>>>> d23ebdb2d2facf1088ebbbbfde340648b0b58fd4
>>>>>>> 14c692bad7bea83d50b6c2bbeef94fb1fc87fe22
]