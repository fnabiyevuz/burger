from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.views.generic.detail import DetailView


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context

class AboutView(TemplateView):
    template_name = "main/about.html"


class MenuView(TemplateView):
    template_name = "main/menu.html"


class BlogView(TemplateView):
    template_name = "main/blog.html"


class ContactView(TemplateView):
    template_name = "main/contact.html"


class CartView(TemplateView):
    template_name = "main/cart.html"
    

class ProductDetailView(DetailView):

    model = Products
    template_name = 'main/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context