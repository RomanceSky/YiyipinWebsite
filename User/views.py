from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.contrib.auth.models import User
# Create your views here.

"""
login_index
"""

from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse

def Index(request):
    if request.method == 'POST':
        if  User.objects.get(username = request.POST['username']):
            return render_to_response('index.html')            
    return render_to_response('login.html',{'p':'1'}, context_instance=RequestContext(request))

    #return HttpResponse('1')

def test():
    return HttpResponseRedirect(reverse_lazy("User:test"))
    #return render_to_response('index_login.html', {'test':2})
