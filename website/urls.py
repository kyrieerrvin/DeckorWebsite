from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('home.html', views.home, name="home2"),
	path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('portfolio.html', views.portfolio, name="portfolio"),
	path('service.html', views.service, name="service"),
	path('appointment.html', views.appointment, name="appointment"),
]