from django.shortcuts import  render, redirect
from django.http import JsonResponse
from .models import *
from django.contrib import messages #import messages
import json
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
#from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from .forms import CreateUserForm
from .utils import cookieCart, cartData, guestOrder




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
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'menu.html', context)





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

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)



def checkout(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
