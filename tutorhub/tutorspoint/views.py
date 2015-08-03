from django.shortcuts import render, render_to_response
from django.template import RequestContext
from registration.backends.default.views import RegistrationView
from tutorspoint.forms import First_ProfileForm, Second_ProfileForm, FirstFilter, SecondFilter
from tutorspoint.models import First_Profile, Second_Profile, Base_Profile

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
#@login_required
def index(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def First_List(request):
	f = FirstFilter(request.GET, queryset = First_Profile.objects.all())
	return render_to_response('home/first_filter.html', {'filter':f})

def Second_List(request):
	f = SecondFilter(request.GET, queryset = Second_Profile.objects.all())
	return render_to_response('home/second_filter.html', {'filter':f})

class First_RegistrationView(RegistrationView):
	form_class = First_ProfileForm
	template_name = 'registration/registration_form_1.html'

	def register(self, request, **cleaned_data):
		new_user= super(First_RegistrationView, self).register(request, **cleaned_data)
		base_profile = Base_Profile(user = new_user, user_type = "first")
		new_profile = First_Profile(user = new_user, first_name = cleaned_data['first_name'], last_name = cleaned_data['last_name'],
		 phone_number = cleaned_data['phone_number'], pic = cleaned_data['pic'])
		new_profile.save()
		base_profile.save()

		return new_user


class Second_RegistrationView(RegistrationView):
	form_class = Second_ProfileForm
	template_name = 'registration/registration_form_2.html'

	def register(self, request, **cleaned_data):
		new_user= super(Second_RegistrationView, self).register(request, **cleaned_data)
		base_profile = Base_Profile(user = new_user, user_type = "second")
		new_profile = Second_Profile(user = new_user, first_name = cleaned_data['first_name'], last_name = cleaned_data['last_name'],
		 phone_number = cleaned_data['phone_number'], pic = cleaned_data['pic'])
		new_profile.save()
		base_profile.save()

		return new_user
