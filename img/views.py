from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .models import ProfilePic


def getgit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profileusername = request.POST['profileusername']
            url = 'https://github.com/' + profileusername
            try:
                r = requests.get(url)
                soup = BeautifulSoup(r.content)
                imagelink = soup.find('img', {'alt': 'Avatar'})['src']
                new_github = ProfilePic(profileusername=profileusername, imagelink=imagelink, username=request.user.username)
                new_github.save()
                messages.success(request, 'Foto do perfil encontrada e salva')
                return redirect('getgit')
            except:
                messages.error(request, 'Usuário não encontrado')

        return render(request, 'getgit.html')
    else:
        return redirect('login')



def getface(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profileusername = request.POST['profileusername']
            url = 'https://facebook.com/' + profileusername
            try:
                r = requests.get(url)
                soup = BeautifulSoup(r.content)
                print(soup)
                imagelink = soup.find('g', {'image': 'url(#jsc_c_4)'})['xlink:href']
                print('oi'+imagelink)
                new_github = ProfilePic(profileusername=profileusername, imagelink=imagelink, username=request.user.username)
                new_github.save()
                messages.success(request, 'Foto do perfil encontrada e salva')
                return redirect('getface')
            except:
                messages.error(request, 'Usuário não encontrado')

        return render(request, 'getface.html')
    else:
        return redirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já cadastrado')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já cadastrado')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'As senhas não conferem')
            return redirect('register')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Credenciais inválidas')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def images(request):
    username = request.user.username
    pics_to_display = ProfilePic.objecs.filter(username=username)
    return render(request, 'images.html', {'pics_to_display': pics_to_display})
