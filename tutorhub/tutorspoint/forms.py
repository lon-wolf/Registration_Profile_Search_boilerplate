from django import forms
from django.contrib.auth.models import User
from tutorspoint.models import Teacher_Profile, Student_Profile
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile
from django.utils.translation import ugettext_lazy as _

class Teacher_ProfileForm(RegistrationForm):
	class Meta:
		model = Teacher_Profile
		fields = ('first_name', 'last_name','qual','phone_number',)


class Student_ProfileForm(RegistrationForm):
	class Meta:
		model = Student_Profile
		fields = ('first_name', 'last_name','qual','phone_number',)