from django.shortcuts import  render, redirect


from django.contrib import messages #import messages


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
#from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from .forms import CreateUserForm




def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)




def home(request):
    return render(request,'home.html',{})

def menu(request):
    return render(request,'menu.html',{})

def blog(request):
    return render(request,'blog.html',{})

def blogsingle(request):
    return render(request,'blog-single.html',{})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


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
