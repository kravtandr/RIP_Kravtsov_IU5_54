from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from rk.models import employee
from rk.models import department


def index(request):
    departments = department.objects.all()
    emps = employee.objects.all()
    return render(request, "index.html", {"departments": departments, "emps": emps})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        dl = department()
        dl.name = request.POST.get("name_department") 
        dl.save()
    return HttpResponseRedirect("/")


def create_emp(request):
    if request.method == "POST":
        d = employee()
        d.name = request.POST.get("name")
        d.sallary = request.POST.get("sallary")
        d.departmentID = department.objects.get(name=request.POST.get("departmentID"))
        d.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        emp = employee.objects.get(id=id)

        if request.method == "POST":
            emp.name = request.POST.get("name")
            emp.sallary = request.POST.get("sallary")
            emp.departmentID = department.objects.get(name=request.POST.get("departmentID"))
            emp.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"emp": emp})
    except employee.DoesNotExist:
        return HttpResponseNotFound("<h2>emp not found</h2>")


def edit_department(request, id):
    try:
        dep = department.objects.get(id=id)

        if request.method == "POST":
            dep.name = request.POST.get("name")
            dep.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_department.html", {"department": dep})
    except department.DoesNotExist:
        return HttpResponseNotFound("<h2>departmentrary not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        emp = employee.objects.get(id=id)
        emp.delete()
        return HttpResponseRedirect("/")
    except employee.DoesNotExist:
        return HttpResponseNotFound("<h2>emp not found</h2>")


def delete_department(request, id):
    try:
        dep = department.objects.get(id=id)
        dep.delete()
        return HttpResponseRedirect("/")
    except employee.DoesNotExist:
        return HttpResponseNotFound("<h2>departmentrary not found</h2>")