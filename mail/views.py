from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView, View, CreateView
from mail.forms import SendMailForm
from mail.models import SendMail
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages



def Home(request):
	send_form = SendMailForm()
	if request.method == "POST":
		subject = request.POST.get("subject", "")
		message = request.POST.get("message", "")
		from_mail = request.POST.get("from_mail", "")
		to_mail = request.POST.get("to_mail", "")
		if subject and message and from_mail and to_mail:
			try:
				send_form = SendMailForm(request.POST)
				if send_form.is_valid():
					send_mail(subject, message, from_mail, [to_mail])
					print(subject, message, from_mail, [to_mail])
					messages.success(request, "Message sent successfully")
					send_form.save()
				else:
					messages.error(request, "Document deleted.")
					return render(request, "index.html")
			except BadHeaderError:
				print("Error")
				return HttpResponse("Invalid header found.")
			return render(request, "index.html")

		else:
			return HttpResponse("Make sure all fields are entered and valid.")

		
	context = {
		'send_form': send_form
	}
	return render(request, "index.html", context)