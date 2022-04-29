from django.shortcuts import render
from django.http import HttpResponse
from oam_portfolio import views

# Create your views here.
def detail(request):
	context = {'nav':'Detail'}
	template_name = 'oam-templates/detail.html'
	return render(request,template_name,context)

