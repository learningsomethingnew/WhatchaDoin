from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth import logout

# importing method overload user creation form
from accounts.custom.registration_form import UserCreateForm

# Require login
from django.contrib.auth.decorators import login_required


# Login page
def login_page(request):
    return render(request, 'registration/login.html')


# User profile, requires users to login
@login_required(login_url='/login/')
def profile(request):
    options = {'fname': request.user.first_name, 'lname': request.user.last_name, 'email': request.user.email,
               'user': request.user.username}
    context = {
        'authed': request.user.is_authenticated(),
        'username': request.user.username,
        'options': options
    }

    return render(request, 'account/profile.html', context)


# User Registration
def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreateForm(request.POST)
        print(request.POST)

        if form.is_valid():
            print(form)
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreateForm()

    return render(
        request,
        "registration/register.html",
        {'form': form}
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')