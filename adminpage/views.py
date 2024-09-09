from django.shortcuts import render, redirect
from .forms import GalleryForm
from .models import Gallery, Contact
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.

def admin_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('admin-home')
        else:
            messages.success(request,"Invalid User")
            return render(request, 'admin/login.html')
    return render(request, 'admin/login.html')

def signout(request):
    logout(request)
    return redirect('login')

def is_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff,login_url='/login/')
def add_gallery(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        alt = request.POST.get('alt')

        if alt and image:
            instance = Gallery(alt=alt,img=image)
            instance.save()
            return redirect('admin-home')
    return render(request,'admin/add_gallery.html')
@user_passes_test(is_staff,login_url='/login/')
def admin_home(request):
    contact = Contact.objects.all()
    gallery = Gallery.objects.all()
    context={
        'contact':contact,
        'gallery':gallery
    }
    return render(request, 'admin/home.html',context)