from django.shortcuts import render, render_to_response
from django.template import RequestContext
from registration.backends.default.views import RegistrationView
from tutorspoint.forms import Teacher_ProfileForm, Student_ProfileForm
from tutorspoint.models import Teacher_Profile, Student_Profile, Base_Profile

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def check(request):
	diff = request.POST['diff']
	if diff == 'teacher':
		return HttpResponseRedirect('/teacher-register/')
	if diff == 'student':
		return HttpResponseRedirect('/student-register/')
	if diff == 'lookteacher' :
		return render(request, 'home/search_teacher.html')
	if diff == 'lookstudent':
		return render(request, 'home/search_student.html')

#@login_required
def index(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

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
