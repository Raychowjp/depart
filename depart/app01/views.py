from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.
def depart(request):
    departments = models.Department.objects.all()

    return render(request, 'depart.html', {"queryset": departments})

def add_depart(request):
    if request.method == 'GET':
        return render(request, 'add_depart.html')
    title = request.POST.get('title')
    count = request.POST.get('count')
    models.Department.objects.create(title=title, count=count)
    return redirect('/depart/')

def delete_depart(request):
    de_id = request.GET.get('id')
    models.Department.objects.filter(id=de_id).delete()
    return redirect('/depart/')


def edit_depart(request):
    if request.method == 'GET':
        depart_id = request.GET.get('id')
        depart_object = models.Department.objects.filter(id=depart_id).first()
        return render(request, 'edit_depart.html', {"depart_object": depart_object})
    depart_id = request.GET.get('id')
    title = request.POST.get('title')
    count = request.POST.get('count')
    models.Department.objects.filter(id=depart_id).update(title=title, count=count)
    return redirect('/depart/')