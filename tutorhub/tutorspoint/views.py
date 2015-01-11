from django.shortcuts import render
from registration.backends.default.views import RegistrationView
from tutorspoint.forms import Teacher_ProfileForm, Student_ProfileForm
from tutorspoint.models import Teacher_Profile, Student_Profile

# Create your views here.
class Teacher_RegistrationView(RegistrationView):
	form_class = Teacher_ProfileForm
	template_name = 'registration/registration_form_t.html'

	def register(self, request, **cleaned_data):
		new_user= super(Teacher_RegistrationView, self).register(request, **cleaned_data)

		new_profile = Teacher_Profile(user = new_user, first_name = cleaned_data['first_name'], last_name = cleaned_data['last_name'],
			qual = cleaned_data['qual'], phone_number = cleaned_data['phone_number'])
		new_profile.save()

		return new_user


class Student_RegistrationView(RegistrationView):
	form_class = Student_ProfileForm
	template_name = 'registration/registration_form_s.html'

	def register(self, request, **cleaned_data):
		new_user= super(Student_RegistrationView, self).register(request, **cleaned_data)

		new_profile = Student_Profile(user = new_user, first_name = cleaned_data['first_name'], last_name = cleaned_data['last_name'],
			qual = cleaned_data['qual'], phone_number = cleaned_data['phone_number'])
		new_profile.save()

		return new_user