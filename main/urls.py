from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('menu/', MenuView.as_view()),
    path('blog/', BlogView.as_view()),
    path('contact/', ContactView.as_view()),
    path('cart/', CartView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),

    path('add-cart/', add_cart),
    path('count-cart/', count_cart),
    path('delete-item/', delete_item),
    path('checkout/', checkout),
]