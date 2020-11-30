from django.shortcuts import render
from .models import Cart
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class CartListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = 'carts/carts_list.html'
    ordering = ['-created']
    cart = Cart.objects.all()
    context_object_name = 'carts'

    def get_context_data(self, *args, **kwargs):
        context = super(CartListView, self).get_context_data(*args, **kwargs)
        return context

cart_list_view = CartListView.as_view()

class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'carts/carts_detail.html'
    

cart_detail_view = CartDetailView.as_view()

class CartCreateView(LoginRequiredMixin,CreateView):
    model = Cart
    template_name = 'carts/carts_form.html'
    #fields = ['pk', 'item', 'customer', 'price', 'price_dec', 'merchant', 'merchant_email', 'created']
    fields = ['pk', 'item', 'customer', 'created']

cart_create_view = CartCreateView.as_view()


class CartUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cart
    #template_name = 'products/product_form.html'
    # fields = ['pk','item', 'customer', 'price', 'price_dec', 'merchant', 'merchant_email', 'created']
    fields = ['pk', 'item', 'customer', 'created']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False

cart_update_view = CartUpdateView.as_view()

class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cart
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('carts_list')
    
    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False

cart_delete_view = CartDeleteView.as_view()


