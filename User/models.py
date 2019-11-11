from django.db import models

# Create your models here.
from django.contrib.auth.models import User


USER_CHOICE = (
   ('Customer', 'Customer'),
   ('Dealer', 'Dealer')
)

def upload_location(instance, filename):
	ProfileModel = instance.__class__
	new_id = ProfileModel.objects.order_by("id").last().id + 1
	locate = "%s/%s" %(new_id, filename)
	return locate

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=20, choices=USER_CHOICE, null=True)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True)
	content = models.TextField()
	def __str__(self):
		return self.user.username