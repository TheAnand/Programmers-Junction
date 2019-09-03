from django.shortcuts import render

def introduction(request):
    return render(request,'programmingcourses/html/introduction.html')

def basic_tags(request):
    return render(request,'programmingcourses/html/basic_tags.html')

def elements(request):
    return render(request,'programmingcourses/html/elements.html')

def attribute(request):
    return render(request,'programmingcourses/html/attribute.html')

def formatting(request):
    return render(request,'programmingcourses/html/formatting.html')

def meta_tags(request):
    return render(request,'programmingcourses/html/meta_tags.html')

def comment(request):
    return render(request,'programmingcourses/html/comment.html')

def image(request):
    return render(request,'programmingcourses/html/image.html')

def table(request):
    return render(request,'programmingcourses/html/table.html')

def list(request):
    return render(request,'programmingcourses/html/list.html')

def link(request):
    return render(request,'programmingcourses/html/link.html')

def block(request):
    return render(request,'programmingcourses/html/block.html')

def classes(request):
    return render(request,'programmingcourses/html/classes.html')

def id(request):
    return render(request,'programmingcourses/html/id.html')

def form(request):
    return render(request,'programmingcourses/html/form.html')

def stylesheet(request):
    return render(request,'programmingcourses/html/stylesheet.html')

def javascript(request):
    return render(request,'programmingcourses/html/javascript.html')