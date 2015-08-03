from django import forms
from django.contrib.auth.models import User
from django.db import models
from tutorspoint.models import First_Profile, Second_Profile
from registration.forms import RegistrationFormUniqueEmail
from registration.models import RegistrationProfile
from django.utils.translation import ugettext_lazy as _
import django_filters

class First_ProfileForm(RegistrationFormUniqueEmail):
	class Meta:
		model = First_Profile
		fields = ('first_name', 'last_name','phone_number','pic',)


class Second_ProfileForm(RegistrationFormUniqueEmail):
	class Meta:
		model = Second_Profile
		fields = ('first_name', 'last_name','phone_number','pic',)


class FirstFilter(django_filters.FilterSet):
	filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_type': 'icontains',
            }
        }
    }
	class Meta:
		model  = First_Profile
		fields = ('first_name', 'last_name')


		
class SecondFilter(django_filters.FilterSet):
	filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_type': 'icontains',
            }
        }
    }
	class Meta:
		model  = Second_Profile
		fields = ('first_name', 'last_name')