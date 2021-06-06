from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Subscriber
from .forms import SubscriberForm

def SubscriberEmail (request):
    form = SubscriberForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()

    return render(request, 'main/main.html',locals())