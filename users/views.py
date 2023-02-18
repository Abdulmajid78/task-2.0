from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProfilesModel
from .forms import  ProfileForm, UserForm

@login_required
def ProfileView(request):
    user = get_object_or_404(ProfilesModel, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=user)
    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

