from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import User, Volunteer, Organization

from .forms import VolunteerCreationModelForm, OrganizationCreationModelForm

def register(request):
    return render(request, 'registration/registration.html')

class VolunteerRegistrationView(CreateView):
    model = User
    form_class = VolunteerCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register_as_volunteer.html'

class OrganizationRegistrationView(CreateView):
    model = User
    form_class = OrganizationCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register_as_organization.html'

class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'volunteer/list.html'
    context_object_name = 'volunteers'

class OrganizationListView(ListView):
    model = Organization
    template_name = 'organization/list.html'
    context_object_name = 'organizations'

class VolunteerDetailView(DetailView):
    model = Volunteer
    template_name = 'volunteer/detail.html'
    context_object_name = 'volunteer'

class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'organization/detail.html'
    context_object_name = 'organization'

class VolunteerUpdateView(UpdateView):
    model = Volunteer
    template_name = 'volunteer/update.html'
    context_object_name = 'volunteer'
    fields = ('phone_number', 'email', 'bio', 'image', )

class OrganizationUpdateView(UpdateView):
    model = Volunteer
    template_name = 'organization/update.html'
    context_object_name = 'organization'
    fields = ('address', 'phone_number', 'email', 'bio', 'image', )

class VolunteerDeleteView(DeleteView):
    model = User
    template_name = 'volunteer/delete.html'
    success_url = reverse_lazy('volunteer/list')

class OrganizationDeleteView(DeleteView):
    model = User
    template_name = 'organization/delete.html'
    success_url = reverse_lazy('organization/list')
