from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db import models
from .models import *

from User.models import *
# Create your views here.
def blog_index(request):
    article = Article.objects.all()
    return render_to_response("book_detail.html",  {"book_detail": article})
    #return render_to_response("book_detaillist.html",  {"book_detail": article})

def blog_index1(request):
    
    article = Article.objects.all()

    return render_to_response("book_detaillist.html",  {"book_detail": article})

