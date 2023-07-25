from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message + " \n\nSent by " + message_email, # message
			message_email, # from email
			['aethernether99@gmail.com'],
			fail_silently=False # To Email
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


def about(request):
	return render(request, 'about.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def service(request):
	return render(request, 'service.html', {})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_service = request.POST['your-service']
		your_message = request.POST['your-message']
		
		# send an email
		appointment = "Name: " + your_name + " \nPhone: " + your_phone + " \nEmail: " + your_email + " \nAddress: " + your_address + " \nService: " + your_service + " \nSchedule: " + your_schedule + " \nMessage: " + your_message

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			[your_email, 'aethernether99@gmail.com'], # To Email
			)
		
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_message': your_message
			})

	else:
		return render(request, 'home.html', {})