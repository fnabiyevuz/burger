from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"


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
    