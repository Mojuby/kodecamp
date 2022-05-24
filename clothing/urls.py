from django.urls import path
from .views import home, women, men

urlpatterns = [
    path('homepage/', home),
    path('women-clothing/', women),
    path('men-clothing/', men),
]
