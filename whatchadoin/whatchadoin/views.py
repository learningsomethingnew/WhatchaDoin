from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from accounts.views import login, profile, register

def login(request):
    return HttpResponseRedirect('/accounts/login/')

def register(request):
    return HttpResponseRedirect('/accounts/register/')

def profile(request):
    return HttpResponseRedirect('/accounts/profile/')