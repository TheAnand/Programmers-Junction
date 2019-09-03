from django.shortcuts import render
from .models import Contactus
# Create your views here.
def index(request):
    return render(request,'programmingcourses/index.html')

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        mo_number=request.POST.get('mobile_number','')
        msg=request.POST.get('message','')
        contactus=Contactus(name=name,email=email,mobile_number=mo_number,message=msg)
        contactus.save()
        return render(request, 'programmingcourses/thankyou.html')
    return render(request,'programmingcourses/contactus.html')

def aboutus(request):
    return render(request,'programmingcourses/aboutus.html')

def courses(request):
    return render(request,'programmingcourses/courses.html')

def cpp(request):
    return render(request,'programmingcourses/cpp.html')

def c(request):
    return render(request,'programmingcourses/c.html')

def java(request):
    return render(request,'programmingcourses/java.html')

def python(request):
    return render(request,'programmingcourses/python.html')

def html(request):
    return render(request,'programmingcourses/html.html')

def css(request):
    return render(request,'programmingcourses/css.html')



