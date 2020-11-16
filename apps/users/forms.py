from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Volunteer, Organization, User



class VolunteerCreationModelForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    # date_joined = forms.DateTimeField()
    email = forms.EmailField(required=True)
    bio = forms.CharField(required=True)
    image = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_volunteer = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        # user.date_joined = self.cleaned_data.get('date_joined')
        user.email = self.cleaned_data.get('email')
        user.bio = self.cleaned_data.get('bio')
        user.image = self.cleaned_data.get('image')
        user.save()
        volunteer = Volunteer.objects.create(user=user)
        volunteer.first_name = self.cleaned_data.get('first_name')
        volunteer.last_name = self.cleaned_data.get('last_name')
        volunteer.phone_number = self.cleaned_data.get('phone_number')
        # volunteer.date_joined = self.cleaned_data.get('date_joined')
        volunteer.email = self.cleaned_data.get('email')
        volunteer.bio = self.cleaned_data.get('bio')
        volunteer.image = self.cleaned_data.get('image')
        volunteer.save()
        return user


class OrganizationCreationModelForm(UserCreationForm):
    name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    # date_joined = forms.DateTimeField()
    email = forms.EmailField(required=True)
    bio = forms.CharField(required=True)
    image = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_volunteer = True
        user.is_staff = True
        user.name = self.cleaned_data.get('name')
        user.address = self.cleaned_data.get('address')
        user.phone_number = self.cleaned_data.get('phone_number')
        # user.date_joined = self.cleaned_data.get('date_joined')
        user.email = self.cleaned_data.get('email')
        user.bio = self.cleaned_data.get('bio')
        user.image = self.cleaned_data.get('image')
        user.save()
        organization = Organization.objects.create(user=user)
        organization.name = self.cleaned_data.get('name')
        organization.address = self.cleaned_data.get('address')
        organization.phone_number = self.cleaned_data.get('phone_number')
        # organization.date_joined = self.cleaned_data.get('date_joined')
        organization.email = self.cleaned_data.get('email')
        organization.bio = self.cleaned_data.get('bio')
        organization.image = self.cleaned_data.get('image')
        organization.save()
        return user

