from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="glavnaya"),
    path("registration/", views.register, name="registration"),
    path('login/', views.login_request, name="login"),
    path('profile/', views.profile, name="profile"),
    path('delete/', views.delete_user, name="delete"),
    path('logout/', views.logout_request, name="logout"),
    path('delete/<int:color_id>/', views.delete_color, name='delete_color'),
    path('edit/<int:palette_id>/', views.edit_palette, name='edit_palette'),
    path('save_palette/<int:palette_id>/', views.save_palette, name='save_palette'),
]