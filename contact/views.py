from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def addContact(request):
    if request.method=='POST':
        new_contact=Contact(
            fullname = request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['e-mail'],
           phone_no=request.POST['phone-number'],
            address=request.POST['address']
        )
        new_contact.save() 
        return render('contact:index')
    return render(request, 'new.html')