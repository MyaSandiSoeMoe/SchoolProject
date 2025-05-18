from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *

# Create your views here.
from django.shortcuts import render
def indexView(request):
    course = Course.objects.all()
    teacher = Teacher.objects.all()
    context = {'course':course, 'teacher': teacher}
    return render (request, 'index.html',context) 

def contactView(request):
    return render (request, 'contact.html')

def courseView(request):
    course = Course.objects.all()
    context = {'course':course}
    return render(request, 'courses.html',context)

def aboutView(request):
    return render(request, 'about.html')

def trainerView(request):
    return render(request, 'trainers.html')
        
def addCourse(request):
    course = CourseModelForm()
    if request.method == "POST":
        course = CourseModelForm(request.POST, request.FILES)
        if course.is_valid():
            course.save()

            return redirect('/course/')
        else:
            return HttpResponse('Error')
    else:
        course = CourseModelForm()
        return render(request,  'addcourse.html', {'course': course})

def addTeacher(request):
    teacher = TeacherModelForm()
    if request.method == "POST":
        teacher = TeacherModelForm(request.POST, request.FILES)
        if teacher.is_valid():
            teacher.save()

            return redirect('/trainer/')
        else:
            return HttpResponse('Error')
    return render(request, 'addteacher.html', {'teacher': teacher})   

def courses(request):
    course_data = Course.objects.all()
    context = {'course_data': course_data}
    return render(request, 'courses.html', context )

def trainers(request):
    teacher_data = Teacher.objects.all()
    context = {'teacher_data': teacher_data}
    return render(request, 'trainers.html', context)

# def updatecourse(request, id):
#     data = Course.objects.get(id=id)
#     obj = CourseModelForm(request.POST, request.FILES, instance=data)
#     if obj.is_valid():
#         obj.save()
#     return redirect('/course/')    

# def updateteacher(request, id):
#     data = Teacher.objects.get(id=id)
#     obj = TeacherModelForm(request.POST, request.FILES, instance=data)
#     if obj.is_valid():
#         obj.save()
#     return redirect('/trainer/')

def updateCourse(request, pk):
    course_obj = Course.objects.get(id=pk)
    fm = UpdateCourseFm()
    if request.method == 'POST':
        photo = request.FILES['photo_fm']
        name = request.POST.get('name_fm')
        desc = request.POST.get('desc_fm')
        fee = request.POST.get('fee_fm')
        course = Course.objects.filter(id = pk)
        course.update(photo=photo, name=name, fee=fee, description = desc)
        return redirect('/index/')
    else:
        return render(request, 'updatec.html',{'course_obj': course_obj, 'fm':fm})

    
