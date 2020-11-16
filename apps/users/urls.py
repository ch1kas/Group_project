from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('registration/', register, name='registration'),
    path('register/volunteer/', VolunteerRegistrationView.as_view(), name='register_as_volunteer'),
    path('register/organization/', OrganizationRegistrationView.as_view(), name='register_as_organization'),
    path('volunteer/detail/<int:pk>/', VolunteerDetailView.as_view(), name='volunteer_detail'),
    path('organization/detail/<int:pk>/',OrganizationDetailView.as_view(), name='organization_detail'),
    path('volunteers/', VolunteerListView.as_view(), name='volunteers_list'),
    path('organizations/', OrganizationListView.as_view(), name='organizations_list'),
    path('volunteer/update/<int:pk>/', VolunteerUpdateView.as_view(), name='volunteer_update'),
    path('organization/update/<int:pk>/', OrganizationUpdateView.as_view(), name='organization_update'),
    path('volunteer/delete/<int:pk>/', VolunteerDeleteView.as_view(), name='volunteer_delete'),
    path('organization/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='organization_delete'),
]
