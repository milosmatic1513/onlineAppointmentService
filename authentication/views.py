from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
from django.contrib.auth import authenticate, login,logout
from .forms import CreateUserForm
def login(request):
    context={}
    return render(request, 'authentication/login.html', context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                #check if user exists
                username = form.cleaned_data.get('email')
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'An account with the email: ' + username+" already exists")
                    return redirect('/authentication/register')
                else:
                    form.save()
                    messages.success(request, 'Account was created for ' + username)
                    return redirect('/authentication/login')
            else:
                for error in form.errors.values() :
                    messages.error(request,error[0])
                return redirect('/authentication/register')
        context = {'form':form}
        return render(request, 'authentication/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/authentication/login')
