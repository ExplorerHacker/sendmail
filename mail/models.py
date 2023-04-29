from django.db import models


# Create your models here.
class SendMail(models.Model):
	subject = models.CharField(max_length=500, default="")
	message = models.TextField()
	from_mail = models.EmailField()
	to_mail = models.EmailField()

	def __str__(self):
		return "From " + self.from_mail + " to " + self.to_mail

		