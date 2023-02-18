from django.contrib.auth.views import PasswordResetView
from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),

]