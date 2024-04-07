from django.shortcuts import render, redirect
from .models import Color
from .forms import ColorForm

def index(request):
    colors = Color.objects.all()
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ColorForm()
    return render(request, 'main/index.html', {'colors': colors, 'form': form})

def delete_color(request, color_id):
    color = Color.objects.get(pk=color_id)
    color.delete()
    return redirect('index')
