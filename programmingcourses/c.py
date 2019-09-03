from django.shortcuts import render

def introduction(request):
    return render(request,'programmingcourses/c/introduction.html')

def basic_syntax(request):
    return render(request,'programmingcourses/c/basic_syntax.html')

def data_types(request):
    return render(request,'programmingcourses/c/data_types.html')

def operators(request):
    return render(request,'programmingcourses/c/operators.html')

def decision_making(request):
    return render(request,'programmingcourses/c/decision_making.html')

def loops(request):
    return render(request,'programmingcourses/c/loops.html')

def function(request):
    return render(request,'programmingcourses/c/function.html')

def pointer(request):
    return render(request,'programmingcourses/c/pointer.html')

def string(request):
    return render(request,'programmingcourses/c/string.html')

def structure(request):
    return render(request,'programmingcourses/c/structure.html')

def file_handling(request):
    return render(request,'programmingcourses/c/file_handling.html')

def error_handling(request):
    return render(request,'programmingcourses/c/error_handling.html')

def command_line_argument(request):
    return render(request,'programmingcourses/c/command_line_argument.html')

