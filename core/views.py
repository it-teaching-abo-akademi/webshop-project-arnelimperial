from django.shortcuts import render
from django.views.generic.base import TemplateView
#from django.shortcuts import HttpResponseRedirect, redirect
#from django.views.decorators.cache import never_cache
#from django.urls import reverse
from django.conf import settings


class IndexTemplateView(TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name

client_view = IndexTemplateView.as_view()

