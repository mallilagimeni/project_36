from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def all_in_one(request):
    TFO=TopicForm()
    WFO=WebPageForm()
    ARO=AccessForm()
    d={'TFO':TFO,'WFO':WFO,'ARO':ARO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        WFD=WebPageForm(request.POST)
        ARD=AccessForm(request.POST)
        if TFD.is_valid() and WFD.is_valid() and ARD.is_valid():
            NSO=TFD.save(commit=False)
            NSO.save()
            NSWO=WFD.save(commit=False)
            NSWO.topic_name=NSO
            NSWO.save()
            NSAO=ARD.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()

           
            return HttpResponse('insert successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'all_in_one.html',d)