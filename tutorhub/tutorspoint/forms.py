from django import forms
from django.contrib.auth.models import User
from tutorspoint.models import Teacher_Profile, Student_Profile
from registration.forms import RegistrationFormUniqueEmail
from registration.models import RegistrationProfile
from django.utils.translation import ugettext_lazy as _
import django_filters

class Teacher_ProfileForm(RegistrationFormUniqueEmail):
	class Meta:
		model = Teacher_Profile
		fields = ('first_name', 'last_name','qual','phone_number',)


class Student_ProfileForm(RegistrationFormUniqueEmail):
	class Meta:
		model = Student_Profile
		fields = ('first_name', 'last_name','qual','phone_number',)


class TeacherFilter(django_filters.FilterSet):
	class Meta:
		model  = Teacher_Profile
		fields = ('first_name', 'qual',)

class StudentFilter(django_filters.FilterSet):
	class Meta:
		model  = Student_Profile
		fields = ('first_name', 'qual',)