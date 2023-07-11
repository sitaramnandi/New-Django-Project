from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.form import CustmerForm,ContactUs_Form,BookForm
from django.http import HttpResponseRedirect  
# from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.views import PasswordResetView

##logo
def logo(request):
    return render(request,"testapp/wonderal.html")


#home Page
def home_page(request):
    return render(request,"testapp/home.html")

#location page
@login_required  
def location_page(request):
   
    return render(request,"testapp/location.html")

# Dining page page
@login_required
def dining_page(request):
    return render(request,"testapp/dinging.html")

#galrry

def gallary_page(request):
    return render(request,"testapp/gallary.html")
#gallary dining page
@login_required
def Gallary_dinging_page(request):
    return render(request,"testapp/gallary_diging.html")

#gallary facility page 
@login_required 
def Gallary_facility_page(request):                       
    return render(request,"testapp/gallary_facility.html")

def timming_ticket(request):
    return render(request,"testapp/timming.html")
#facitity
def facility(request):
    return render(request,"testapp/facility.html")

#Contact US
def Contact_us(request):
    form = ContactUs_Form()
    
    if request.method == "POST":
        form = ContactUs_Form(request.POST)
        
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/accounts/login')
    return render(request, "testapp/contactus.html", {'form': form})
def signup_page(request):
    form=CustmerForm()
    if request.method=="POST":
        form=CustmerForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password) #to the  hash password
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,"testapp/signup.html",{"form":form})


def logout_page(request):
    return render(request,"testapp/logout.html")
 

# Booking_page
@login_required
def Book_page(request):
    form=BookForm()
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request,"testapp/Booking.html",{'form':form})

#  Footer Page
def aboutus_page(request):
    return render(request,"testapp/aboutus.html")
# Privacy Policy
def Privacy_Policy(request):
    return render(request,"testapp/Privacy_Policy.html")
#term and conditions
def term_conditions(request):
    return render(request,"testapp/term_conditions.html")

#Refund
def refund(request):
    return render(request,"testapp/refund.html")

#Support
def support(request):
    return render(request,"testapp/support.html")





 