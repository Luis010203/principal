from django.contrib import admin
from .models import Producto,Pedido

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha",)

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha",)

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)