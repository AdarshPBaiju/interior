from django.shortcuts import render,redirect
from adminpage.models import Contact, Gallery

def home(request):
    image = Gallery.objects.all()
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            instance = Contact(name=name,email=email, message=message)
            instance.save()
            return redirect('home')
    return render(request, 'index.html',{'image':image})