from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
class ListaProdutos(ListView):
    model = models.Produto
    template_name= './produto/lista.html'
    context_object_name= 'produtos'

class ProdutoDetalhe(View):
     def get(self,*args, **kwargs):
        return HttpResponse('produtodetelhe')

class AdicionarAoCarrinho(View):
    def get(self,*args, **kwargs):
        return HttpResponse('adcicionaraocarrinho')
    

class RemoverdoCarrinho(View):
    def get(self,*args, **kwargs):
        return HttpResponse('removerdocarrinho')
    

class Carrinho(View):
    def get(self,*args, **kwargs):
        return HttpResponse('carrinho')
    

class Finalizar(View):
    def get(self,*args, **kwargs):
        return HttpResponse('finallizar')
    


