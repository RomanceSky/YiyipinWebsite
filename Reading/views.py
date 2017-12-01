
#-*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from Reading.forms import ProfileForm
from Reading.models import Profile

def SaveProfile(request):
    saved = False

    if request.method == "POST":
        MyProfileForm = ProfileForm(request.POST, request.FILES)#Get the posted form

        if MyProfileForm.is_valid():
            reading = Profile()
            reading.Bookname = MyProfileForm.cleaned_data["Bookname"]
            reading.picture = MyProfileForm.cleaned_data["picture"]
            reading.save()
            saved = True
        else:
            MyProfileForm = Profileform()
        #return HttpResponseRedirect(reverse_lazy("reading"))


        return render(request, 'readingList.html', locals()) 
