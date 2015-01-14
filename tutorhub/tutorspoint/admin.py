from django.contrib import admin
from tutorspoint.models import Teacher_Profile, Student_Profile, Base_Profile
# Register your models here.
admin.site.register(Teacher_Profile)
admin.site.register(Student_Profile)
admin.site.register(Base_Profile)

