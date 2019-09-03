from django.shortcuts import render

def introduction(request):
    return render(request,'programmingcourses/cpp/introduction.html')

def basic_syntax(request):
    return render(request,'programmingcourses/cpp/basic_syntax.html')

def data_types(request):
    return render(request,'programmingcourses/cpp/data_types.html')

def operators(request):
    return render(request,'programmingcourses/cpp/operators.html')

def decision_making(request):
    return render(request,'programmingcourses/cpp/decision_making.html')

def loops(request):
    return render(request,'programmingcourses/cpp/loops.html')

def function(request):
    return render(request,'programmingcourses/cpp/function.html')

def array(request):
    return render(request,'programmingcourses/cpp/array.html')

def basic_input_output(request):
    return render(request,'programmingcourses/cpp/basic_input_output.html')

def classes_and_objects(request):
    return render(request,'programmingcourses/cpp/classes_and_objects.html')

def inheritance(request):
    return render(request,'programmingcourses/cpp/inheritance.html')

def polymorphism(request):
    return render(request,'programmingcourses/cpp/polymorphism.html')

def overlaoding_and_overriding(request):
    return render(request,'programmingcourses/cpp/overloading_and_overriding.html')

def exception_handling(request):
    return render(request,'programmingcourses/cpp/exception_handling.html')