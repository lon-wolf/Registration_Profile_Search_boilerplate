from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import User

class Teacher_Profile(models.Model):
	user = models.ForeignKey(User, unique = True)
	first_name = models.CharField("First Name", max_length = 30, blank = True)
	last_name = models.CharField("Last Name", max_length = 30, blank = True)
	qual = models.CharField("Qualification", max_length = 30, blank = True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField("Phone Number", validators=[phone_regex], blank=True, max_length = 15)

	def __unicode__(self):
		return self.first_name


class Student_Profile(models.Model):
	user = models.ForeignKey(User, unique=True)
	first_name = models.CharField("First Name", max_length = 30, blank = True)
	last_name = models.CharField("Last Name", max_length = 30, blank = True)
	qual = models.CharField("Qualification", max_length = 30, blank = True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField("Phone Number", validators=[phone_regex], blank=True, max_length = 15)

	def __unicode__(self):
		return self.first_name