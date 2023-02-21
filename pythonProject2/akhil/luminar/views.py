from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def testfun(request):
    return render(request,"register.html")
