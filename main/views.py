from django.shortcuts import render, redirect
from .models import Palette

def index(request):
    palettes = Palette.objects.all()
    return render(request, 'main/index.html', {'palettes': palettes})

def delete_color(request, color_id):
    color = Palette.objects.get(pk=color_id)
    color.delete()
    return redirect('index')