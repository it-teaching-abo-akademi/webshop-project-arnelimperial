from django.shortcuts import render
from .models import Purchase
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class PurchaseListView(LoginRequiredMixin,ListView):
    model = Purchase
    template_name = 'purchases/purchases_list.html'
    ordering = ['-created']
    purchase = Purchase.objects.all()
    context_object_name = 'purchases'

    def get_context_data(self, *args, **kwargs):
        context = super(PurchaseListView, self).get_context_data(*args, **kwargs)
        return context

purchase_list_view = PurchaseListView.as_view()

class PurchaseDetailView(LoginRequiredMixin, DetailView):
    model = Purchase
    template_name = 'purchasess/purchases_detail.html'
    

purchase_detail_view = PurchaseDetailView.as_view()

class PurchaseCreateView(LoginRequiredMixin,CreateView):
    model = Purchase
    template_name = 'carts/carts_form.html'
   
    fields = ['pk', 'purchases', 'buyer', 'sellers', 'purchases_price', 'created']

purchase_create_view = PurchaseCreateView.as_view()


class PurchaseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Purchase
    #template_name = 'products/product_form.html'
   
    fields = ['pk', 'purchases', 'buyer', 'sellers', 'purchases_price', 'created']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        purchase = self.get_object()
        if self.request.user == purchase.user:
            return True
        return False

purchase_update_view = PurchaseUpdateView.as_view()

class PurchaseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Purchase
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('purchase_list')
    
    def test_func(self):
        purchase = self.get_object()
        if self.request.user == purchase.user:
            return True
        return False

purchase_delete_view = PurchaseDeleteView.as_view()


