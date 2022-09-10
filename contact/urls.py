from django.urls import path
from .views import Home
app_name='contact'

urlpatterns = [
    path('', Home, name='home'),
]