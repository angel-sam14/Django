from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# def home(request):
#     return HttpResponse('home page')
# def about(request): #http://127.0.0.1:8000/
#     return HttpResponse('About page')
# def student(request):
#     return HttpResponse('Student Page')
# def contact(request):
#     return HttpResponse('Contact Page')
# def services(request):
#     return HttpResponse('Service Page')
# name = 'Akhil'
all_students = [
    {'name':'Akhil', 'age':20, 'mark':80},
    {'name':'Arun', 'age':20, 'mark':40},
    {'name':'Karthik', 'age':21, 'mark':21},
    {'name':'Jinu', 'age':22, 'mark':45},
]
def home(request):
    return render(request, 'index.html',{'std_name':'Akhil'})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')

def students(request):
    return render(request, 'students.html', {'students':all_students})

def contacts(request):
    return render(request, 'contacts.html')

def get_student(request,id):
    student = student.objects.get(id=id)
    # std = None
    # for student in all_students:
    #     if student['name'] == name:
    #         std = student
    return render(request,'student.html',{'student':student})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get['name']
        age = int(request.POST.get['age'])
        mark = int(request.POST.get['mark'])
        course = request.POST.get['course']
        student.objects.create(name=name,age=age,mark=mark,course=course)
        # all_students.append({'name':name,'age':age,'mark':mark,'course':course})
        return redirect('view_students')
    return render(request,'add_student.html')
