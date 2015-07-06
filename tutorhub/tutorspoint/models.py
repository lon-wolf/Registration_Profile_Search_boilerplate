from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import User



class First_Profile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField("Name", max_length = 50, blank = True)
	age = models.IntegerField("Age")
	sex = models.CharField("Sex", max_length = 10, blank = True)
	address1 = models.CharField("Address Line 1", max_length = 100, blank = True)
	address2 = models.CharField("Address Line 2", max_length = 100, blank = True)
	zipcode = models.CharField("ZIP code", max_length = 6, blank = True)
	city = models.CharField("City", max_length = 100, blank = True)
	state = models.CharField("State", max_length = 100, blank = True)
	country = models.CharField("Country", max_length = 100, blank = True)
	qual = models.CharField("Qualification", max_length = 100, blank = True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField("Phone Number", validators=[phone_regex], blank=False, max_length = 15)
	skills = models.CharField(max_length = 100, blank = True)
	mode = models.CharField(max_length = 100, blank = True)
	location = models.CharField("Preferred Locations", max_length = 100, blank = True)
	classes = models.CharField("Preferred Classes", max_length = 100, blank = True)
	subjects = models.CharField("Preferred Subjects", max_length = 100, blank = True)
	exp = models.CharField("Teaching Experience", max_length = 30, blank = True)
	lfee = models.IntegerField(default = -1)
	hfee = models.IntegerField(default = -1)
	pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

	def __unicode__(self):
		return self.name

class Second_Profile(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField("First Name", max_length = 30, blank = True)
	last_name = models.CharField("Last Name", max_length = 30, blank = True)
	qual = models.CharField("Qualification", max_length = 30, blank = True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField("Phone Number", validators=[phone_regex], blank=True, max_length = 15)

	def __unicode__(self):
		return self.first_name

class Base_Profile(models.Model):
	user = models.OneToOneField(User)
	user_type = models.CharField(max_length = 30, blank = True)

	def __unicode__(self):
		return self.user_type
