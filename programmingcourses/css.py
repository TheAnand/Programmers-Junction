from django.shortcuts import render

def introduction(request):
    return render(request,'programmingcourses/css/introduction.html')

def basic_syntax(request):
    return render(request,'programmingcourses/css/basic_syntax.html')

def colors(request):
    return render(request,'programmingcourses/css/colors.html')

def background(request):
    return render(request,'programmingcourses/css/background.html')

def font(request):
    return render(request,'programmingcourses/css/font.html')

def text(request):
    return render(request,'programmingcourses/css/text.html')

def image(request):
    return render(request,'programmingcourses/css/image.html')

def link(request):
    return render(request,'programmingcourses/css/link.html')

def table(request):
    return render(request,'programmingcourses/css/table.html')

def border(request):
    return render(request,'programmingcourses/css/border.html')

def margin(request):
    return render(request,'programmingcourses/css/margin.html')

def list(request):
    return render(request,'programmingcourses/css/list.html')

def padding(request):
    return render(request,'programmingcourses/css/padding.html')

def box_model(request):
    return render(request,'programmingcourses/css/box_model.html')

def height_and_width(request):
    return render(request,'programmingcourses/css/height_and_width.html')

def pseudo_class(request):
    return render(request,'programmingcourses/css/pseudo_class.html')

def pseudo_element(request):
    return render(request,'programmingcourses/css/pseudo_element.html')

def rounded_corner(request):
    return render(request,'programmingcourses/css/rounded_corner.html')
