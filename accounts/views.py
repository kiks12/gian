from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm


def registerpage(request):
    form = RegisterForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.save()
        if user:
            return redirect('/users/')

    context = {
        'form': form,
    }

    return render(request, "auth/register.html", context)


def loginpage(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('homepage')
    context = {
        "form": form
    }
    return render(request, "auth/login.html", context)
