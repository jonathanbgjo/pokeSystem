from django.shortcuts import render, redirect
from ..loginReg_app.models import User
from models import Poke
from django.db.models import Count

# Create your views here.
def poke(request):
	if 'email_address' not in request.session:
		return redirect("/poke")
	context = {
	'user': User.objects.get(id=request.session['user_id']),
	'otherUsers': User.objects.exclude(id=request.session['user_id']),
	'pokedMe': [],
	"works": User.objects.exclude(id=request.session['user_id']).filter(gave=request.session['user_id']),
	'countMe':[],
	'realcountMe':[],
	'output':[]
	}

	idofusers = context['user'].got.all().values('giver__id').distinct()
	for x in idofusers:
		context['pokedMe'].append(User.objects.get(id=x['giver__id']))

	countofusers = context['user'].got.all().values('giver__id')
	for x in countofusers:
		context['countMe'].append(User.objects.get(id=x['giver__id']))

	for x in context['pokedMe']:
		count = 0
		for y in context['countMe']:
			if x.name == y.name:
				count+=1
		str = "{} has poked you {} times".format(x.name, count)
		context['realcountMe'].append(str)
		# context['realcountMe'].append(count)

	return render(request,"pokeExam_app/poke.html", context)
def give(request, user_id):
	Poke.objects.create(giver = User.objects.get(id=request.session['user_id']), receiver = User.objects.get(id=user_id))
	return redirect("/poke")