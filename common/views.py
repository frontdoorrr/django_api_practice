from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class ProductList(ListView):
	model = Product
	template_name = 'common/index.html'

class ProductDetail(DetailView):
	model = Product
	template_name = 'common/detail.html'
