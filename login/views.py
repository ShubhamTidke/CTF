from django.shortcuts import render
#from django.views.generic import TemplateView
from passlib.hash import pbkdf2_sha256
from .models import Team

def index(request):
	return render(request, 'login/index.html')

def home(request):
	if request.method == "POST":
		t = Team(team = request.POST['team_1'])
		if t.team == "":
			return render(request, 'login/index.html',  {'error_team_1': " Cannot be empty"})

		t.user_1 = request.POST['user_1']
		if t.user_1 == "":
			return render(request, 'login/index.html',  {'error_user_1': " Cannot be empty"})
		t.password_1 = pbkdf2_sha256.encrypt(str(request.POST['password_1']), rounds=12000, salt_size=32)
		t.user_2 = request.POST['user_2']
		t.password_2 = pbkdf2_sha256.encrypt(str(request.POST['password_2']), rounds=12000, salt_size=32)
		t.email = request.POST['email_1']
		t.save()
	return render(request, 'login/home.html')
