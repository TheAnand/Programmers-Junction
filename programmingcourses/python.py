from django.shortcuts import render

def introduction(request):
    return render(request,'programmingcourses/python/introduction.html')

def environment_setup(request):
    return render(request,'programmingcourses/python/environment_setup.html')

def basic_syntax(request):
    return render(request,'programmingcourses/python/basic_syntax.html')

def data_types(request):
    return render(request,'programmingcourses/python/data_types.html')

def operators(request):
    return render(request,'programmingcourses/python/operators.html')

def decision_making(request):
    return render(request,'programmingcourses/python/decision_making.html')

def loops(request):
    return render(request,'programmingcourses/python/loops.html')

def function(request):
    return render(request,'programmingcourses/python/function.html')

def modules(request):
    return render(request,'programmingcourses/python/modules.html')

def basic_input_output(request):
    return render(request,'programmingcourses/python/basic_input_output.html')

def exception_handling(request):
    return render(request,'programmingcourses/python/exception_handling.html')

def file_handling(request):
    return render(request,'programmingcourses/python/file_handling.html')

def classes_and_objects(request):
    return render(request,'programmingcourses/python/classes_and_objects.html')

def constructor(request):
    return render(request,'programmingcourses/python/constructor.html')

def inheritance(request):
    return render(request,'programmingcourses/python/inheritance.html')

def overlaoding_and_overriding(request):
    return render(request,'programmingcourses/python/overloading_and_overriding.html')

def data_hiding(request):
    return render(request,'programmingcourses/python/data_hiding.html')

def regular_expression(request):
    return render(request,'programmingcourses/python/regular_expression.html')