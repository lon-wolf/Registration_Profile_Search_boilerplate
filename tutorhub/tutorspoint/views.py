from django.shortcuts import render, render_to_response
from django.template import RequestContext
from registration.backends.default.views import RegistrationView
from tutorspoint.forms import Teacher_ProfileForm, Student_ProfileForm, TeacherFilter, StudentFilter
from tutorspoint.models import Teacher_Profile, Student_Profile, Base_Profile

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
#@login_required
def index(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def Teacher_List(request):
	f = TeacherFilter(request.GET, queryset = Teacher_Profile.objects.all())
	return render_to_response('home/teacher_filter.html', {'filter':f})

def Student_List(request):
	f = StudentFilter(request.GET, queryset = Student_Profile.objects.all())
	return render_to_response('home/student_filter.html', {'filter':f})

class Teacher_RegistrationView(RegistrationView):
	form_class = Teacher_ProfileForm
	template_name = 'registration/registration_form_t.html'

	def register(self, request, **cleaned_data):
		new_user= super(Teacher_RegistrationView, self).register(request, **cleaned_data)
		base_profile = Base_Profile(user = new_user, user_type = "teacher")
		new_profile = Teacher_Profile(user = new_user, first_name = cleaned_data['first_name'], last_name = cleaned_data['last_name'],
			qual = cleaned_data['qual'], phone_number = cleaned_data['phone_number'])
		new_profile.save()
		base_profile.save()

		return new_user


class Student_RegistrationView(RegistrationView):
	form_class = Student_ProfileForm
	template_name = 'registration/registration_form_s.html'

	def register(self, request, **cleaned_data):
		new_user= super(Student_RegistrationView, self).register(request, **cleaned_data)
		base_profile = Base_Profile(user = new_user, user_type = "student")
		new_profile = Student_Profile(user = new_user, first_name = cleaned_data['first_name'], last_name = cleaned_data['last_name'],
			qual = cleaned_data['qual'], phone_number = cleaned_data['phone_number'])
		new_profile.save()
		base_profile.save()

		return new_user
