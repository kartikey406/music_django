from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
import urllib
import json
from django.core.context_processors import csrf
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from  django.shortcuts import RequestContext
from django.contrib.auth.forms import UserCreationForm
from demo1.models import History
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from demo1.script.demoscript import demo_script
# Create your views here.
def home(request):
	return HttpResponseRedirect('/basic')
def last_fm(request):
	args={}
	args.update(csrf(request))
	if request.method=="POST":
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('sucess.html',args)
		else:
			return HttpResponse('username is taken already or password you entered is wrong')

	args['form']= UserCreationForm()
	return  render_to_response('sign.html',args)
def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/game')
	else:
		return HttpResponse('invalid')

	
@login_required	
def game(request):
	
	artist_name=request.POST.get('username','')
	
	if artist_name is not '':
		
		h=History(name=artist_name,user=request.user,hist_date=timezone.now())
		h.save()
	
		try:
			v,z=demo_script(artist_name)
			e=v['toptracks']
			m=z['similarartists']
		except:
			return HttpResponse('error in parsing')
		
		return render_to_response('search.html',{'s':m,'k':e,'full_name':request.user.username}, context_instance=RequestContext(request))
		
	else:
		return  render_to_response('search.html',{'full_name':request.user.username},context_instance=RequestContext(request))
	 
          
def logout(request):
	auth.logout(request)
	
	return HttpResponseRedirect('/basic')
@login_required
def history(request):
	h=History.objects.filter(user=request.user)
	return render_to_response('history.html',{'s':h})
def repeat(request,artist_id=None):
	h=History(name=artist_id,user=request.user,hist_date=timezone.now())
	h.save()
	v,z=demo_script(artist_name)
	e=v['toptracks']
	m=z['similarartists']
	return render_to_response('search.html',{'s':m,'k':e,'full_name':request.user.username}, context_instance=RequestContext(request))

		
	
	
