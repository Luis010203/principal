from .forms import ProductoForm, PedidoForm
from .models import Producto, Pedido
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm,'error':'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('dashboard')
        
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signup.html', {'form':UserCreationForm, 'error':'User already exists'})
        return render(request, 'signup.html', {'form':UserCreationForm, 'error':'Password do not match'})

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'name':request.user})

@login_required
def productos(request):
    productos = Producto.objects.all()

    if request.method == 'GET':
        return render(request,'productos.html',{'name':request.user, 'form': ProductoForm, 'productos': productos})
    else:
        try:
            form = ProductoForm(request.POST)
            new_producto = form.save(commit=False)
            new_producto.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'productos.html', {'name':request.user, 'form': ProductoForm, 'productos': productos, 'error':'Please provide valide data'})

@login_required
def editar_producto(request, producto_id):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, pk=producto_id)
        form=ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'producto': producto, 'form': form})
    else:
        try:
            producto = get_object_or_404(Producto, pk=producto_id)
            form = ProductoForm(request.POST, instance=producto)
            form.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'editar_producto.html', {'producto': producto, 'form': form, 'error': "Error updating task"})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)    
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')

@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()

    if request.method == 'GET':
        return render(request,'pedidos.html',{'name':request.user, 'form': PedidoForm, 'pedidos': pedidos})
    else:
        try:
            form = PedidoForm(request.POST)
            new_pedido = form.save(commit=False)
            new_pedido.save()
            return redirect('pedidos')
        except ValueError:
            return render(request, 'pedidos.html', {'name':request.user, 'form': PedidoForm, 'pedidos': pedidos, 'error':'Please provide valide data'})

@login_required
def editar_pedido(request, pedido_id):
    if request.method == 'GET':
        pedido = get_object_or_404(Pedido, pk=pedido_id)
        form=PedidoForm(instance=pedido)
        return render(request, 'editar_pedido.html', {'pedido': pedido, 'form': form})
    else:
        try:
            pedido = get_object_or_404(Pedido, pk=pedido_id)
            form = PedidoForm(request.POST, instance=pedido)
            form.save()
            return redirect('pedidos')
        except ValueError:
            return render(request, 'editar_pedido.html', {'pedido': pedido, 'form': form, 'error': "Error updating task"})

@login_required
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)    
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos')

@login_required
def signout(request):
    logout(request) 
    return redirect('signin')