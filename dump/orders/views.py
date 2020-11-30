from django.shortcuts import render
from .models import Cart
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class OrdersListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = 'orders/orders_list.html'
    ordering = ['-created_date']
    cart = Cart.objects.all()
    context_object_name = 'cart'

    def get_context_data(self, *args, **kwargs):
        context = super(OrdersListView, self).get_context_data(*args, **kwargs)
        return context

orders_list_view = OrdersListView.as_view()

class OrdersDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'orders/orders_detail.html'
    

orders_detail_view = OrdersDetailView.as_view()

class OrdersCreateView(LoginRequiredMixin,CreateView):
    model = Cart
    template_name = 'orders/orders_form.html'
    fields = ['buyer', 'item', 'quantity', 'sold', 'created_date', 'updated_date',]

orders_create_view = OrdersCreateView.as_view()


class OrdersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cart
    #template_name = 'products/product_form.html'
    fields = ['buyer', 'item', 'quantity', 'sold', 'created_date', 'updated_date',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False

orders_update_view = OrdersUpdateView.as_view()

class OrdersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cart
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('orders_list')
    
    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False

orders_delete_view = OrdersDeleteView.as_view()


