from django.shortcuts import render
from .models import Product
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    ordering = ['-created_date']
    product = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductsListView, self).get_context_data(*args, **kwargs)
        return context

products_list_view = ProductsListView.as_view()

class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products/products_detail.html'
    

products_detail_view = ProductsDetailView.as_view()

class ProductsCreateView(LoginRequiredMixin,CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['title', 'description', 'price', 'seller', 'created_date', 'updated_date', 'product_image',]



products_create_view = ProductsCreateView.as_view()


class ProductsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    #template_name = 'products/product_form.html'
    fields = ['title', 'description', 'price', 'created_date', 'updated_date', 'product_image',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        return False

products_update_view = ProductsUpdateView.as_view()

class ProductsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('products_list')
    
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        return False

products_delete_view = ProductsDeleteView.as_view()


