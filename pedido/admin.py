from django.contrib import admin
from . import models
# Register your models here.
class ItemPedidoInline(admin.TabularInline):
    model= models.ItemPedido
    extra=1

class ProdutoAdmin(admin.ModelAdmin):
    inlines= [
        ItemPedidoInline
    ]
admin.site.register(models.Pedido, ProdutoAdmin)
admin.site.register(models.ItemPedido)