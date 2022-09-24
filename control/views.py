from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from main.models import Shops

class CallCenterView(TemplateView):
    template_name = "manage/call-center.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_cooker:
            return redirect('/cooker/')
        elif request.user.is_deliver:
            return redirect('/deliver/')
        elif request.user.is_cashier:
            return redirect('/cashier/')
        else:
            return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Shops.objects.filter(status="booked")
        return context


def change_sts(request):
    st = request.GET['st']
    pk = request.GET['pk']
    w = request.GET['w']

    sh = Shops.objects.get(id=pk)
    sh.status = st
    sh.save()

    if w == 'cen':
        url = '/call-center/'
    elif w=='co':
        url = '/cooker/'
    elif w=='de':
        url = '/deliver/'
    elif w=='ca':
        url = '/cashier/'
    return redirect(url)

class CookerView(TemplateView):
    template_name = "manage/cooker.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_call_center:
            return redirect('/call-center/')
        elif request.user.is_deliver:
            return redirect('/deliver/')
        elif request.user.is_cashier:
            return redirect('/cashier/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Shops.objects.filter(status="accepted")
        return context


class DeliverView(TemplateView):
    template_name = "manage/deliver.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_call_center:
            return redirect('/call-center/')
        elif request.user.is_cooker:
            return redirect('/cooker/')
        elif request.user.is_cashier:
            return redirect('/cashier/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Shops.objects.filter(status="sent")
        return context


class CashierView(TemplateView):
    template_name = "manage/cashier.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_call_center:
            return redirect('/call-center/')
        elif request.user.is_cooker:
            return redirect('/cooker/')
        elif request.user.is_deliver:
            return redirect('/deliver/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Shops.objects.filter(status="sold")
        context['cashier'] = 'active'
        return context


class AllBoolsView(TemplateView):
    template_name = "manage/all-books.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_call_center:
            return redirect('/call-center/')
        elif request.user.is_cooker:
            return redirect('/cooker/')
        elif request.user.is_deliver:
            return redirect('/deliver/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Shops.objects.all()
        context['all_books'] = 'active'
        return context
