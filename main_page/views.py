from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'home.html',{})

def menu(request):
    return render(request,'menu.html',{})

def blog(request):
    return render(request,'blog.html',{})

def blogsingle(request):
    return render(request,'blog-single.html',{})

def login(request):
    return render(request,'log-in.html',{})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']


        #send Email
        send_mail(
            message_name, #Subject
            message, #message_email
            message_email, #from Email
            ['pritamdebnath297@gmail.com'], #to email
        )
        return render(request,'contact.html',{'message_name':message_name})
    else:
        return render(request,'contact.html',{})


def about(request):
    return render(request,'about.html',{})

def services(request):
    return render(request,'services.html',{})
