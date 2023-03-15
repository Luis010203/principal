from django import forms
from .models import Producto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un nombre'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe una categoria'}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cantidad', 'producto', 'usuario']
        widgets = {
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe una cantidad'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }