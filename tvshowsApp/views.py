from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def redirectMain(request):
    return redirect('/shows/')

def showAdd(request):
    return render(request, "showAdd.html")

def showDetails(request, showid):
    context = {
        "show" : show.objects.get(id=showid)
    }
    return render(request, "showDetails.html", context)

def showEdit(request, showid):
    context = {
        "show" : show.objects.get(id=showid)
    }
    return render(request, "showEdit.html", context)

def showList(request):
    context = {
        'shows' : show.objects.all()
    }
    return render(request, "showList.html", context)

def createShow(request):
    errors = show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new/')
    else:
        created_show = show.objects.create(title=request.POST['title'],network=request.POST['network'],
        description=request.POST['description'],release_date=request.POST['release_date'])

        return redirect(f'/shows/{created_show.id}')

def alterShow(request, showid):
    this_show = show.objects.get(id=showid)
    this_show.title=request.POST['title']
    this_show.network=request.POST['network']
    this_show.release_date=request.POST['release_date']
    this_show.description=request.POST['description']
    this_show.save()

    return redirect(f'/shows/{showid}')

def deleteShow(request, showid):
    this_show = show.objects.get(id=showid)
    this_show.delete()
    return redirect('/shows/')