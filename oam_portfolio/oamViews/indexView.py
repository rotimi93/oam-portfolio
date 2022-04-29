from django.shortcuts import render
from django.http import HttpResponse
from oam_portfolio import views

# Create your views here.
def home(request):
	template_name = 'oam-templates/cv.html'
	context = {'nav':'curriculum-vitae'}
	return render(request,template_name, context)

