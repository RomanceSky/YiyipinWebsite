from django.shortcuts import render

# Create your views here.

"""
login_index
"""

from django.shortcuts import render_to_response
from django.http import HttpResponse

def Index(request):
    #return render_to_response('User/login.html',{'p':'1'},context_isinstance=RequestContext(request)
    return HttpResponse('1')


