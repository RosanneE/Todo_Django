from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from.models import Icon, List

def index(request):
    myicons = Icon.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myicons': myicons,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template= loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def add_list(request):
    template= loader.get_template('add_list.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    a = request.POST['url']
    b = request.POST['description']
    c = request.POST['time']
    icon = Icon(icon_img=a, icon_description=b,time_todo=c)
    icon.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    icon = Icon.objects.get(id=id)
    icon.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    myicons = Icon.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myicons': myicons,
    }
    return HttpResponse(template.render(context, request))

def add_listrecord(request):
    a = request.POST['list_name']
    b = request.POST['list_description']
    list = List(list_name=a, list_description=b,)
    list.save()
    return HttpResponseRedirect(reverse('index'))

def updaterecord(request, id):
    url = request.POST['url']
    description = request.POST['description']
    time = request.POST['time']
    icon = Icon.objects.get(id=id)
    icon.icon_img = url
    icon.icon_description = description
    icon.time_todo = time
    icon.save()
    return HttpResponseRedirect(reverse('index'))