from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Volunteer, Organization


class VolunteerCreationModelForm(UserCreationForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'phone_number',
                  'email', 'bio', 'image',
                  ]


class OrganizationCreationModelForm(UserCreationForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'phone_number',
                  'email', 'bio', 'image',
                  ]
