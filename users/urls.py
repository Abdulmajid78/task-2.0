<<<<<<< HEAD
from django.urls import path
from .views import ProfileView


urlpatterns = [
    path('profile/', ProfileView, name='profile')
=======
from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
>>>>>>> d23ebdb2d2facf1088ebbbbfde340648b0b58fd4
]