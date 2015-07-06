from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

from tutorspoint.views import First_RegistrationView
from tutorspoint.views import Second_RegistrationView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tutorspoint.views.index', name='home'),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^first-register/',First_RegistrationView.as_view(),
                           name='registration_register_1'),
    url(r'^second-register/',Second_RegistrationView.as_view(),
                           name='registration_register_2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^t-list/', 'tutorspoint.views.First_List', name = 'first_list'),
    url(r'^s-list/', 'tutorspoint.views.Second_List', name = 'second_list'),
    url(r'^pic_folder/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}),
)
