from django.shortcuts import render
from .models import Merchandise
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class MerchandiseListView(ListView):
    model = Merchandise
    template_name = 'merchandises/merchandises_list.html'
    ordering = ['-created_date']
    item = Merchandise.objects.all()
    context_object_name = 'merchandises'

    def get_context_data(self, *args, **kwargs):
        context = super(MerchandiseListView, self).get_context_data(*args, **kwargs)
        return context

merchandise_list_view = MerchandiseListView.as_view()

class MerchandiseDetailView(DetailView):
    model = Merchandise
    template_name = 'merchandises/merchandises_detail.html'
    

merchandise_detail_view = MerchandiseDetailView.as_view()

class MerchandiseCreateView(LoginRequiredMixin,CreateView):
    model = Merchandise
    template_name = 'items/items_form.html'
    fields = ['title', 'description', 'price', 'price_dec','merchant', 'created_date', 'updated_date', 'product_image', 'on_stock']



merchandise_create_view = MerchandiseCreateView.as_view()


class MerchandiseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Merchandise
    #template_name = 'products/product_form.html'
    fields = ['title', 'description', 'price', 'price_dec','merchant', 'created_date', 'updated_date', 'product_image', 'on_stock']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        merchandise = self.get_object()
        if self.request.user == merchandise.user:
            return True
        return False

merchandise_update_view = MerchandiseUpdateView.as_view()

class MerchandiseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Merchandise
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('merchandises_list')
    
    def test_func(self):
        merchandise = self.get_object()
        if self.request.user == merchandise.user:
            return True
        return False

merchandise_delete_view = MerchandiseDeleteView.as_view()


