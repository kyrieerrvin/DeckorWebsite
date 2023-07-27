from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		contact_message = "<em><u><h3>This is an auto-generated response to your email sent to us.</h3></u></em> <br>Did you send this email: <br>" + message + "<br><br><br> <h4><strong>If you are aware of this message, reply with '<u>YES</u>'.</strong> <br> <strong>If you are not aware of this message, please <u>do not reply</h4></u>.</strong>"


		# send an email
		send_mail(
			message_name, # subject
			contact_message, # message
			message_email, # from email
			[message_email, 'aethernether99@gmail.com'],
			fail_silently=False, # To Email
			html_message=contact_message
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


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
		your_message = request.POST['your-message']
		selected_date = request.POST['your-date']

		date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
		formatted_date = date_obj.strftime('%B %d, %Y')
		
		# send an email
		appointment = "Name: " + your_name + " \nPhone: " + your_phone + " \nEmail: " + your_email + " \nAddress: " + your_address + " \n\nSchedule: " + your_schedule + " \nAppointment date: " + formatted_date + " \nMessage: " + your_message

		send_mail(
			'Appointment Request Details', # subject
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
			'your_message': your_message,
			'formatted_date' : formatted_date
			})



	else:
		return render(request, 'home.html', {})