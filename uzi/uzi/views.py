from django.shortcuts import redirect
from django.shortcuts import render,HttpResponse,redirect 

def login_redirect(request):
    return redirect('/account/profile')

def about(request):
    return render(request,'accounts/about.html')