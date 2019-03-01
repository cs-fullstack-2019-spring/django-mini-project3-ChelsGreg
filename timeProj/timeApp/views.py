from django.shortcuts import render, get_object_or_404, redirect
from .models import TimeModel
from .forms import TimeForm

# Create your views here.

# LIST TEACHERS
def index(request):
    allTeachers = TimeModel.objects.all()

    return render(request, 'timeApp/index.html', {'allTeachers': allTeachers})

# DISPLAY ENTRIES OF SELECTED TEACHER
def teacherInfo(request, id):
    teacher = get_object_or_404(TimeModel, pk=id)
    newEntry = TimeForm(request.POST or None)
    if newEntry.is_valid():
        newEntry.save()
        return redirect('index')
    context ={
        'teacher': teacher,
        'newEntry': newEntry
    }
    return render(request, 'timeApp/info.html', context)

# NEW TEACHER ENTRY
def newTeacher(request):
    newEntry = TimeForm(request.POST or None)
    if newEntry.is_valid():
        newEntry.save()
        return redirect('index')
    return render(request, 'timeApp/newTeacher.html', {'newEntry': newEntry})

# EDIT TEACHER
def edit(request, id):
    teacher = get_object_or_404(TimeModel, pk=id)
    editForm = TimeForm(request.POST or None, instance= teacher)
    if editForm.is_valid():
        editForm.save()
        return redirect('index')

#DELETE
def delete(request, id):
    teacher = get_object_or_404(TimeModel, pk=id)
    if request.method == "POST":
        teacher.delete()
        return redirect('index')

    return render(request, 'timeApp/delete.html', {'holla': teacher})

# TO SHOW SCHOOLS HOURS
def schoolHours(request, id):
    school = TimeModel.objects.filter('school')
    hours = get_object_or_404(school, pk=id)
    context={
        'hours': hours,
        'school': school,
    }
    return render(request, 'timeApp/schoolHours.html', context)


