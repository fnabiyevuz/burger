from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from django.views.generic.detail import DetailView
from django.http import JsonResponse

class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['burgers'] = Products.objects.filter(category__image = 'burger')
        context['fries'] = Products.objects.filter(category__image = 'fries')
        return context

class AboutView(TemplateView):
    template_name = "main/about.html"


class MenuView(TemplateView):
    template_name = "main/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context


class BlogView(TemplateView):
    template_name = "main/blog.html"


class ContactView(TemplateView):
    template_name = "main/contact.html"


class CartView(TemplateView):
    template_name = "main/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop = Shops.objects.filter(client=self.request.user, status='opened')
        if len(shop) > 0:
            shp = shop[0]
        else:
            shp = None
        context['shop'] = shp
        return context
    

class ProductDetailView(DetailView):

    model = Products
    template_name = 'main/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def add_cart(request):
    id = request.GET['id']
    user = request.user
    print(id, user)

    shop = Shops.objects.filter(client_id=user, status='opened')
    prod = Products.objects.get(id=id)
    if prod.discount:
        price = prod.discount
    else:
        price = prod.price
    if len(shop) > 0:
        shp = shop[0]
    else:
        shp = Shops.objects.create(client=user)
    shpi = ShopItems.objects.filter(product_id=id, shop=shp)
    if len(shpi) > 0:
        shpi = shpi[0]
        shpi.quantity +=1
        shpi.total += price
        shpi.save()
    else:
        ShopItems.objects.create(product=prod, shop=shp, total=price)
    
    shp.total += price
    shp.save()
    if request.GET.get('m'):
        return redirect('/{}/'.format(request.GET.get('m')))
    else:
        return redirect('/')



def count_cart(request):
    data = {
        'count': ShopItems.objects.filter(shop__client=request.user, shop__status='opened').count(),
    }
    return JsonResponse(data)

def delete_item(request):
    id = request.GET['id']
    try:
        item = ShopItems.objects.get(id=id)
    except:
        return redirect('/cart')
    if item.shop.client == request.user:
        item.delete()
    else:
        return redirect('/cart')


def checkout(request):
    try:
        shop = request.GET['shp']
        shop = Shops.objects.get(id=shop)
    except:
        pass
    
    if shop.client == request.user:
        shop.status = 'booked'
        shop.save()
    
    return redirect('/cart/')
