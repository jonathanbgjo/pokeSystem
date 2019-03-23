from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
# Create your views here.
def index(request):
	#User.objects.all().delete()
	return render(request, "loginReg_app/index.html")

def register(request):
	results = User.objects.validate(request.POST)
	if results['status'] == True:
		user = User.objects.creator(request.POST)
		messages.success(request, "User has successfully been created")
	else:
		for error in results['errors']:
			messages.error(request, error)
	return redirect("/")

def login(request):
	results = User.objects.loginVal(request.POST)
	if results['status'] == False:
		messages.error(request, "Please check your email and password")
		return redirect("/")
	else:
		request.session["email_address"] = results["user"].email_address
		request.session["name"] = results["user"].name
		request.session['user_id'] = results["user"].id
		return redirect("/poke")

def logout(request):
	request.session.flush()
	return redirect("/")