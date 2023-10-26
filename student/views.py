from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from student.forms import StudentForm

from student.models import Student

# Create your views here.
def list_students(request):
    students = Student.objects.all()
    return render(request, 'student/list_student.html', {'students': students})
        
def create_student(request):
    context = {'action': 'Criar'}
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:list-student'))
        else:
            context['form'] = form
            return render(request, 'student/form_student.html', context)
    else:
        context['form'] = StudentForm()
        return render(request, 'student/form_student.html', context)

def detail_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student/detail_student.html', {'student': student})

def edit_student(request, student_id):
    context = {'action': 'Editar'}
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:list-student'))
        else:
            context['form'] = form
            return render(request, 'disk/form_student.html', context)
    else:
        student = Student.objects.get(pk=student_id)
        form = StudentForm(instance=student)
        context['form'] = form

        return render(request, 'student/form_student.html', context)
    
def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('student:list-student'))