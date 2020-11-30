from django.shortcuts import render
from .models import Item
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from .tasks import sleepy, send_to_sender


class ItemListView(ListView):
    model = Item
    template_name = 'items/items_list.html'
    ordering = ['-created_date']
    item = Item.objects.all()
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super(ItemListView, self).get_context_data(*args, **kwargs)
        return context

item_list_view = ItemListView.as_view()

class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/items_detail.html'
    

item_detail_view = ItemDetailView.as_view()

class ItemCreateView(LoginRequiredMixin,CreateView):
    model = Item
    template_name = 'items/items_form.html'
    fields = ['title', 'description', 'price', 'vendor', 'created_date', 'updated_date', 'product_image',]



item_create_view = ItemCreateView.as_view()


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    #template_name = 'products/product_form.html'
    fields = ['title', 'description', 'price', 'vendor', 'created_date', 'updated_date', 'product_image',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.user:
            return True
        return False

item_update_view = ItemUpdateView.as_view()

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    # template_name = 'products/product_form.html'
    success_url = reverse_lazy('item_list')
    
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.user:
            return True
        return False

item_delete_view = ItemDeleteView.as_view()


