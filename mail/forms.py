from django import forms
from mail.models import SendMail


class SendMailForm(forms.ModelForm):
	class Meta:
		model = SendMail
		fields = '__all__'