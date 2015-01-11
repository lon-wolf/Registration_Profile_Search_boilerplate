from django.conf.urls import patterns, include, url
from django.contrib import admin



from tutorspoint.views import Teacher_RegistrationView
from tutorspoint.views import Student_RegistrationView

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'signups.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'accounts/register/$', 
       # MyRegistrationView.as_view(), 
      #  name = 'registration_register'),
	#url(r'^profile/', include('profiles.urls')),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^teacher-register/',Teacher_RegistrationView.as_view(),
                           name='registration_register_t'),
    url(r'^student-register/',Student_RegistrationView.as_view(),
                           name='registration_register_s'),

    url(r'^admin/', include(admin.site.urls)),
)
