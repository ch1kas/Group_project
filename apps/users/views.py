from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import VolunteerCreationModelForm, OrganizationCreationModelForm

class VolunteerRegistrationView(CreateView):
    form_class = VolunteerCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class OrganizationRegistrationView(CreateView):
    form_class = OrganizationCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'