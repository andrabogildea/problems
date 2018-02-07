import zipfile
import fnmatch

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import get_template

from . import forms

# Create your views here.


class ZipFormView(View):
    form_class = forms.ZipForm
    template_name = 'form.html'
    template_email = 'email.txt'
    email_subject = 'Zip summary for {name}'
    email_from = 'zipsummary@example.org'


    def get(self, request):
        empty_form = self.form_class()
        return render(request, self.template_name, {'form': empty_form})

    def post(self, request):
        zip_form = self.form_class(request.POST, request.FILES)
        if zip_form.is_valid():
            cleaned_data = zip_form.cleaned_data
            to, pattern = cleaned_data['email'], cleaned_data['pattern']
            try:
                self.send_summary(to, request.FILES['zipfile'], pattern)
            except zipfile.BadZipFile:
                messages.error(request, 'Invalid zip file.')
            else:
                messages.success(request, 'Summary sent.')
            return HttpResponseRedirect(reverse('zipform'))
        return render(request, self.template_name, {'form': zip_form})


    def send_summary(self, to, zip_file, pattern):
        email_template = get_template(self.template_email)
        email_body = email_template.render(context={
            'files': filter_filenames(zip_file, pattern),
            'name': zip_file.name,
            'pattern': pattern,
        })
        subject = self.email_subject.format(name=zip_file.name)
        send_mail(subject, email_body, self.email_from, [to])


def filter_filenames(zip_file, pattern):
    filenames = []
    with zipfile.ZipFile(zip_file, 'r') as f:
        filenames = f.namelist()
        if pattern:
            filenames = fnmatch.filter(filenames, pattern)
    return filenames
