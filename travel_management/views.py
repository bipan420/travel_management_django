from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def home(request):
    return render(request,'home.html')

def package(request):
    return render(request,'package.html')

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def blog(request):
	return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
	return render(request, 'register.html')

def signin(request):
	return render(request,'login.html')

