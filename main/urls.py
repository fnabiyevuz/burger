from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('menu/', MenuView.as_view()),
    path('blog/', BlogView.as_view()),
    path('contact/', ContactView.as_view()),
    path('cart/', CartView.as_view()),
]