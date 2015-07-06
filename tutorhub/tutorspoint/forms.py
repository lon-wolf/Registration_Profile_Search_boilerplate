from django import forms
from django.contrib.auth.models import User
from django.db import models
from tutorspoint.models import First_Profile, Second_Profile
from registration.forms import RegistrationFormUniqueEmail
from registration.models import RegistrationProfile
from django.utils.translation import ugettext_lazy as _
import django_filters

SKILL_CHOICES = [('Academics','Academics'), ('Competetions','Competetions'), ('Special_Skills','Special Skills')]
MODE_CHOICES = [('Online','Online'), ('Tutions_At_Home','Tutions At Home')]
class First_ProfileForm(RegistrationFormUniqueEmail):
	skills = forms.MultipleChoiceField(choices=SKILL_CHOICES, widget=forms.CheckboxSelectMultiple(), label = "Category of Teaching Skills")
	mode = forms.MultipleChoiceField(choices=MODE_CHOICES, widget=forms.CheckboxSelectMultiple(), label = "Mode of Teaching")
	class Meta:
		model = First_Profile
		exclude = ('user','skills','mode',)


class Second_ProfileForm(RegistrationFormUniqueEmail):
	class Meta:
		model = Second_Profile
		fields = ('first_name', 'last_name','qual','phone_number',)


class FirstFilter(django_filters.FilterSet):
	skl = forms.MultipleChoiceField(choices=SKILL_CHOICES, widget=forms.CheckboxSelectMultiple(), label = "Category of Teaching Skills")
	hfee = django_filters.NumberFilter(lookup_type='lt')
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
		fields = ('classes', 'subjects','location','hfee',)


		
class SecondFilter(django_filters.FilterSet):
	class Meta:
		model  = Second_Profile
		fields = ('first_name', 'qual',)