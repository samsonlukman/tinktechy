from django.shortcuts import render
from .models import NewMessage

def index(request):
    return render(request, "website/index.html")

def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_message = NewMessage(name=name, email=email, message=message)

        new_message.save()

        return render(request, "website/index.html", {"message": "Message Sent Successfully"})