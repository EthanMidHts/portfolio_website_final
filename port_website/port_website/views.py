from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import ContactForm
from django.urls import reverse_lazy
from django.template import loader
from django.template import RequestContext


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def projects(request):
    template = loader.get_template('projects.html')

    return HttpResponse(template.render({}, request))


def experience(request):
    template = loader.get_template('experience.html')
    return HttpResponse(template.render({}, request))


def resume(request):
    template = loader.get_template('resume.html')
    return HttpResponse(template.render({}, request))


def contact(request):
    template = loader.get_template('contact.html')

    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        form_data = {
            'name': name,
            'email': email,
            'message': message,
        }
        message = '''
            From:\n\t\t{}\n
            Message:\n\t\t{}\n
            Email:\n\t\t{}\n
            '''.format(form_data['name'], form_data['message'], form_data['email'])
        send_mail('You got a mail!', message, '', ['ethanhunterswe@gmail.com'])
    return HttpResponse(template.render({}, request))


