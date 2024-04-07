from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('delete/<int:color_id>/', views.delete_color, name='delete_color'),
]