from django.urls import path
from .views import VolunteerRegistrationView, OrganizationRegistrationView

app_name = 'users'

urlpatterns = [
    path('accounts/register/volunteer/', VolunteerRegistrationView.as_view(), name='register_as_volunteer'),
    path('accounts/register/organization/', OrganizationRegistrationView.as_view(), name='register_as_organization'),
]
