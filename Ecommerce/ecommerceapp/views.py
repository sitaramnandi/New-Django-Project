from django.shortcuts import render

# Create your views here.
# nav bar  
def home_page(request):
    return render(request,"ecommerceapp/home.html")

def contact(request):
    return render(request,"ecommerceapp/contact.html")

def about(request):
    return render(request,"ecommerceapp/about.html")