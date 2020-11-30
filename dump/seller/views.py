from django.shortcuts import render
from .models import ProductSold
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class SellerListView(LoginRequiredMixin, ListView):
    model = ProductSold
    template_name = 'seller/seller_list.html'
    ordering = ['-created_date']
    seller = ProductSold.objects.all()
    context_object_name = 'seller'

    def get_context_data(self, *args, **kwargs):
        context = super(SellerListView, self).get_context_data(*args, **kwargs)
        return context

seller_list_view = SellerListView.as_view()

class SellerDetailView(LoginRequiredMixin, DetailView):
    model = ProductSold
    template_name = 'seller/seller_detail.html'
    

seller_detail_view = SellerDetailView.as_view()

class SellerCreateView(LoginRequiredMixin,CreateView):
    model = ProductSold
    template_name = 'seller/seller_form.html'
    fields = ['product_name', 'created_date', 'updated_date',]

seller_create_view = SellerCreateView.as_view()


class SellerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProductSold
    #template_name = 'products/product_form.html'
    fields = ['product_name', 'created_date', 'updated_date',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        seller = self.get_object()
        if self.request.user == seller.user:
            return True
        return False

seller_update_view = SellerUpdateView.as_view()

class SellerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProductSold
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('seller_list')
    
    def test_func(self):
        seller = self.get_object()
        if self.request.user == seller.user:
            return True
        return False

seller_delete_view = SellerDeleteView.as_view()


