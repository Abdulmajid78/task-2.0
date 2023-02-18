from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout




def logout_view(request):
    logout(request)
    return redirect('main:home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
#
# {% if error_message %}
#     <p>{{ error_message }}</p>
# {% endif %}
#
# <form method="post" action="{% url 'login' %}">
#     {% csrf_token %}
#
#     <input type="text" id="username" name="username"><br>
#
#
#
#     <input type="password" id="password" name="password"><br>
#     <input type="submit" value="Login">
# </form>
