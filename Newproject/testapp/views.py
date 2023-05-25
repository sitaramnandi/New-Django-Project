from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.form import CustmerForm
from django.http import HttpResponseRedirect
# Create your views here.
#home Page
def home_page(request):
    return render(request,"testapp/home.html")

#location page
# @login_required
def location_page(request):
    
    return render(request,"testapp/location.html")

# Dining page page
def dining_page(request):
    return render(request,"testapp/dinging.html")

def timming_ticket(request):
    return render(request,"testapp/timming.html")


#login page
def login_page(request):
    return render (request,"testapp/login.html")

def signup_page(request):
    form=CustmerForm()
    if request.method=="POST":
        form=CustmerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,"testapp/signup.html",{"form":form})


def logout_page(request):
    
    return render(request,"testapp/logout.html")
 
 