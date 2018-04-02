from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import logout as __logout, login as __login, authenticate
from django.contrib.auth.models import User

def index(request):
    return render(request, 'unAventonApp/index.html')


def login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            ## se autentico bien
            __login(request, user)
            return HttpResponseRedirect('/')
        else:
            ## algun dato esta mal
            context['error'] = True

    return render(request, 'unAventonApp/login.html', context)


def signIn(request):
    return render(request, 'unAventonApp/signIn.html')


def signInRegister(request):
    if request.method == 'POST':
        r = request.POST
        user = User.objects.create_user(r['email'],r['email'],r['password'])
        user.save()
        return render(request, 'unAventonApp/signin_success.html')
    return HttpResponseRedirect('signin')

def logout(request):
    __logout(request)
    return HttpResponseRedirect('/')
