from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_uppercase, ascii_lowercase



def home(request):
    return render(request, 'templates/home.html')

def about(request):
    return render(request, 'templates/about.html')

def password(request):
    characters = list(ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'templates/password.html', {'password': thepassword})