from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

from tutorspoint.views import Teacher_RegistrationView
from tutorspoint.views import Student_RegistrationView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tutorspoint.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^teacher-register/',Teacher_RegistrationView.as_view(),
                           name='registration_register_t'),
    url(r'^student-register/',Student_RegistrationView.as_view(),
                           name='registration_register_s'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^t-list/', 'tutorspoint.views.Teacher_List', name = 'teacher_list'),
    url(r'^s-list/', 'tutorspoint.views.Student_List', name = 'student_list'),
    url(r'^pic_folder/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}),
)
