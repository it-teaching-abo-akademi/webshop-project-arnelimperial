from django.shortcuts import render
from .models import ProductBought
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class BuyerListView(ListView):
    model = ProductBought
    template_name = 'buyer/buyer_list.html'
    ordering = ['-created_date']
    buyer = ProductBought.objects.all()
    context_object_name = 'buyer'

    def get_context_data(self, *args, **kwargs):
        context = super(BuyerListView, self).get_context_data(*args, **kwargs)
        return context

buyer_list_view = BuyerListView.as_view()

class BuyerDetailView(DetailView):
    model = ProductBought
    template_name = 'buyer/buyer_detail.html'
    

buyer_detail_view = BuyerDetailView.as_view()

class BuyerCreateView(LoginRequiredMixin,CreateView):
    model = ProductBought
    template_name = 'buyer/buyer_form.html'
    fields = ['product_name', 'created_date', 'updated_date',]

buyer_create_view = BuyerCreateView.as_view()


class BuyerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProductBought
    #template_name = 'products/product_form.html'
    fields = ['product_name', 'created_date', 'updated_date',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        buyer = self.get_object()
        if self.request.user == buyer.user:
            return True
        return False

buyer_update_view = BuyerUpdateView.as_view()

class BuyerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProductBought
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('buyer_list')
    
    def test_func(self):
        buyer = self.get_object()
        if self.request.user == buyer.user:
            return True
        return False

buyer_delete_view = BuyerDeleteView.as_view()


