from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
	title = 'contact'
	form = contactForm(request.POST)
	context = {'title': title, 'form': form,}

	if request.method == 'POST':
		if form.is_valid():
			name = form.cleaned_data['name']
			comment = form.cleaned_data['comment']
			subject = 'Message from Walesblog.com'
			message = '%s %s' %(comment, name)
			emailFrom = form.cleaned_data['email']
			emailTo = [settings.EMAIL_HOST_USER]
			send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
			title = "Thanks!"
			confirm_message = "Thanks for your message. We will get right back to you."
			context = {'title': title, 'confirm_message':confirm_message,}
	else:
		form = contactForm()
	return render(request, 'contact.html', context)
    


    
    
	        
	            
		    
    

   