from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html")

def admin(request):
    return render(request, "home/admin/admin_login.html")

def customer(request):
    return render(request, "home/customer/cust_home.html")
    
def worker(request):
    return render(request, "home/worker/worker_login.html")