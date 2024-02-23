from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.

def register(req):
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
        
    else :
        form = CreateUserForm(req.POST)
    context ={
        'form' : form,
    }
    return render(req,'user/register.html',context)

def profile(req):
    return render(req,'user/profile.html')