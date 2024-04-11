from django.shortcuts import render, redirect
from .models import Palette, UserPalette
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden)
from django.views.decorators.csrf import csrf_exempt

from .forms import NewUser
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

def index(request):
    palettes = Palette.objects.all()
    return render(request, 'main/index.html', {'palettes': palettes})


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        else:
            return render(request, 'main/registrationform.html', {"register_form":form})
    form = NewUser()
    return render(request=request, template_name="main/registrationform.html", context={"register_form":form})

@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logged in")
                return redirect("glavnaya")
            else:
                return render(request, 'main/login.html', {"login_form":form})
        else:
            return render(request, 'main/login.html', {"login_form":form})
    form = AuthenticationForm()
    return render(request, 'main/login.html', {"login_form":form})

def logout_request(request):
    logout(request)
    return redirect('glavnaya')

def profile(request):
    return render(request, 'main/profile.html')

def delete_user(request):
    context = {}
    
    if not request.user.is_authenticated:
        return redirect("login")

    try:
        user = request.user
        user.delete()
        return redirect("glavnaya")
    except Exception as e: 
        context['msg'] = 'Something went wrong!'

    return render(request, 'main/profile.html', context=context)

def edit_palette(request, palette_id):
    palette = Palette.objects.get(id=palette_id)
    return render(request, 'main/edit.html', {'palette': palette, 'palette_id': palette_id})

@login_required
def save_palette(request, palette_id):
    if request.method == "POST":
        palette = Palette.objects.get(id=palette_id)
        user_palette, created = UserPalette.objects.get_or_create(user=request.user)
        user_palette.palettes.add(palette)
        user_palette.save()
        print(user_palette.palettes)
        return redirect('profile')

def delete_color(request, color_id):
    color = Palette.objects.get(pk=color_id)
    color.delete()
    return redirect('index')