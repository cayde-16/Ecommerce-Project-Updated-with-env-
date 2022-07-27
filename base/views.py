from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import datetime 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def main(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        cart = json.loads(request.COOKIES['cart'])
        print('Cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':-1, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quanity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quanity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quanity']

                item = {
                    'product':{
                        'id': product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                    },
                'quanity':cart[i]['quanity'],
                'get_total':total,
                }
                items.append(item)
            except:
             pass

    products = Product.objects.all()[0:3]
    latest_products = Product.objects.all().reverse()[3:9]


    context = {'latest_products':latest_products,'products': products, 'cartItems':cartItems, 'items':items}
    return render(request, 'base/main.html', context)

   
def logoutUser(request):
    logout(request)
    return redirect('main')


def product(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        cart = json.loads(request.COOKIES['cart'])
        print('Cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':-1, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quanity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quanity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quanity']

                item = {
                    'product':{
                        'id': product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                    },
                'quanity':cart[i]['quanity'],
                'get_total':total,
                }
                items.append(item)
            except:
             pass

    context = {'cartItems':cartItems, 'products':products}
    return render(request,'base/products.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        cart = json.loads(request.COOKIES['cart'])
        print('Cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':-1, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quanity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quanity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quanity']

                item = {
                    'product':{
                        'id': product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                        'description':product.description
                    },
                'quanity':cart[i]['quanity'],
                'get_total':total,
                }
                items.append(item)
            except:
             pass
    context = {"items":items, "order":order, 'cartItems':cartItems}
    return render(request, 'base/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        cart = json.loads(request.COOKIES['cart'])
        print('Cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':-1, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quanity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quanity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quanity']

                item = {
                    'product':{
                        'id': product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                    },
                'quanity':cart[i]['quanity'],
                'get_total':total,
                }
                items.append(item)
            except:
             pass

    if request.method == 'POST':
        return redirect('main')


    context = {'cartItems':cartItems, 'order':order, 'items':items}
    return render(request, 'base/checkout.html', context)

def details(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()[:3]

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        cart = json.loads(request.COOKIES['cart'])
        print('Cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':-1, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quanity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quanity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quanity']

                item = {
                    'product':{
                        'id': product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                    },
                'quanity':cart[i]['quanity'],
                'get_total':total,
                }
                items.append(item)
            except:
             pass

    context = {'order':order, 'items':items, 'product':product, 'products':products, 'cartItems':cartItems}
    return render(request, 'base/details.html', context)

def login_user(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        cart = json.loads(request.COOKIES['cart'])
        print('Cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':-1, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quanity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quanity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quanity']

                item = {
                    'product':{
                        'id': product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                    },
                'quanity':cart[i]['quanity'],
                'get_total':total,
                }
                items.append(item)
            except:
             pass
        

    form = UserCreationForm()

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'An Error as Occured during registration')

    context = {'order':order, 'items':items,'cartItems':cartItems, 'form':form}
    return render(request,'base/login.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quanity = (orderItem.quanity + 1)
    elif action == 'remove':
        orderItem.quanity = (orderItem.quanity - 1)

    orderItem.save()
    if orderItem.quanity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
    else:
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print('User is not logged in')
    return JsonResponse('Payment Complete!', safe=False)
