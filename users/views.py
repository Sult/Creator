from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from forms import RegistrationForm




def login_user(request):
    """Logs a user into the application."""
    auth_form = AuthenticationForm(None, request.POST or None)
	
    # The form itself handles authentication and checking to make sure password and such are supplied.
    if auth_form.is_valid():
       login(request, auth_form.get_user())
       return HttpResponseRedirect(reverse('index'))
 
    return render(request, 'login.html', {'auth_form': auth_form})


# account views
# Register new user
def register_user(request):
	# False till someone fills in and sends
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = RegistrationForm()
	
	return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
	

#Logout
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('login_user'))
	


def index(request):
	# See if user is logged in
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login_user'))
		
	return render(request, 'index.html')
