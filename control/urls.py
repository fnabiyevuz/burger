from django.urls import path
from .views import *

urlpatterns = [
    path('call-center/', CallCenterView.as_view()),
    path('cooker/', CookerView.as_view()),
    path('deliver/', DeliverView.as_view()),
    path('cashier/', CashierView.as_view()),
    path('cashier/all-books/', AllBoolsView.as_view()),
    path('change_sts/', change_sts),
]