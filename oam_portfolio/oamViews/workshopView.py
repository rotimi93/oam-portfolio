from django.shortcuts import render
from django.http import HttpResponse
from oam_portfolio import views

# Create your views here.
def ws(request):
	context = {'nav':'workShop'}
	template_name = 'oam-templates/ws.html'
	return render(request,template_name,context)

