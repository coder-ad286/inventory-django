from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(req):
    return render(req,'dashboard/index.html')

@login_required
def staff(req):
    return render(req,'dashboard/staff.html')

@login_required
def product(req):
    return render(req,"dashboard/product.html")

@login_required
def order(req):
    return render(req,"dashboard/order.html")