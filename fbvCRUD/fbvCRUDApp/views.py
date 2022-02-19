from django.shortcuts import render, redirect
from fbvCRUDApp.models import Student
from fbvCRUDApp.forms import StudentForm


# Create your views here.
def getStudents(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'student': students})


def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'create.html', {'form': form})


def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')
