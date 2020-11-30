from django.shortcuts import render
from .models import Initial
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class InitialListView(LoginRequiredMixin,ListView):
    model = Initial
    template_name = 'orders/orders_list.html'
    ordering = ['-created_date']
    init = Initial.objects.all()
    context_object_name = 'init'

    def get_context_data(self, *args, **kwargs):
        context = super(InitialListView, self).get_context_data(*args, **kwargs)
        return context

initial_list_view = InitialListView.as_view()

class InitialDetailView(LoginRequiredMixin, DetailView):
    model = Initial
    template_name = 'initial/initial_detail.html'
    

initial_detail_view = InitialDetailView.as_view()

class InitialCreateView(LoginRequiredMixin,CreateView):
    model = Initial
    template_name = 'initial/initial_form.html'
    fields = ['name','created_date',]

initial_create_view = InitialCreateView.as_view()


# class OrdersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Cart
#     #template_name = 'products/product_form.html'
#     fields = ['buyer', 'item', 'quantity', 'sold', 'created_date', 'updated_date',]

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         cart = self.get_object()
#         if self.request.user == cart.user:
#             return True
#         return False

# orders_update_view = OrdersUpdateView.as_view()

# class OrdersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Cart
#     # template_name = 'products/product_form.html'
#     success_url = reverse_lazy('orders_list')
    
#     def test_func(self):
#         cart = self.get_object()
#         if self.request.user == cart.user:
#             return True
#         return False

# orders_delete_view = OrdersDeleteView.as_view()


