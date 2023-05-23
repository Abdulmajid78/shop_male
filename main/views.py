from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .models import BannerModel
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = BannerModel.objects.filter(status=True)
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm
        return context


class ContactCreateView(CreateView):
    form_class = ContactForm

    def get_success_url(self):
        return reverse('main:contact')
