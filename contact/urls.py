from django.urls import path
from .views import index, addContact
app_name='contact'

urlpatterns = [
    path('',index, name='index'),
    path('addContact/',addContact, name='addContact'),
]